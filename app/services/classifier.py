from __future__ import annotations

import json
import os
import time
from typing import Dict, List, Tuple

from app.utils.logging import get_logger

logger = get_logger(__name__)

try:
    from openai import OpenAI  # Optional dependency
except Exception:  # pragma: no cover
    OpenAI = None


CATEGORY_KEYWORDS: Dict[str, List[str]] = {
    "network_issue": [
        "vpn",
        "wifi",
        "network",
        "internet",
        "router",
        "latency",
        "dns",
        "connectivity",
        "packet loss",
        "slow connection",
        "offline",
    ],
    "identity_access": [
        "login",
        "password",
        "signin",
        "sign in",
        "account",
        "access",
        "mfa",
        "2fa",
        "locked out",
        "authentication",
    ],
    "hardware_issue": [
        "laptop",
        "desktop",
        "screen",
        "battery",
        "keyboard",
        "mouse",
        "monitor",
        "overheating",
        "shutdown",
        "printer",
    ],
    "software_issue": [
        "install",
        "application",
        "app",
        "bug",
        "crash",
        "error",
        "update",
        "slow",
        "freeze",
        "license",
    ],
    "security_issue": [
        "phishing",
        "malware",
        "virus",
        "suspicious",
        "breach",
        "compromised",
        "ransomware",
        "spam",
        "security",
        "threat",
    ],
    "billing_issue": [
        "invoice",
        "billing",
        "charge",
        "payment",
        "refund",
        "subscription",
        "receipt",
        "overcharged",
        "pricing",
    ],
}

CATEGORY_ORDER = [
    "security_issue",
    "network_issue",
    "identity_access",
    "hardware_issue",
    "software_issue",
    "billing_issue",
    "other",
]


def _normalize_text(text: str) -> str:
    return " ".join(text.strip().lower().split())


def _keyword_hits(text: str, keywords: List[str]) -> List[str]:
    hits = []
    for kw in keywords:
        if kw in text:
            hits.append(kw)
    return hits


def _rule_based_classification(subject: str, message: str) -> Dict[str, object]:
    text = _normalize_text(f"{subject} {message}")

    scores: Dict[str, int] = {category: 0 for category in CATEGORY_ORDER}
    matched: Dict[str, List[str]] = {category: [] for category in CATEGORY_ORDER}

    for category, keywords in CATEGORY_KEYWORDS.items():
        hits = _keyword_hits(text, keywords)
        matched[category] = hits
        scores[category] += len(hits) * 2

    best_category = "other"
    best_score = 0

    for category in CATEGORY_ORDER:
        if scores[category] > best_score:
            best_score = scores[category]
            best_category = category

    if best_score == 0:
        confidence = 0.58
        reasoning = "No strong keyword match found. Defaulting to other."
    else:
        confidence = min(0.99, 0.62 + (best_score * 0.08))
        selected_hits = matched.get(best_category, [])[:5]
        reasoning = (
            f"Matched keywords for {best_category}: "
            + ", ".join(selected_hits)
            if selected_hits
            else f"Predicted {best_category} based on text similarity."
        )

    return {
        "category": best_category,
        "confidence": round(confidence, 2),
        "reasoning": reasoning,
    }


def _openai_classification(subject: str, message: str, channel: str) -> Dict[str, object] | None:
    api_key = os.getenv("OPENAI_API_KEY")
    use_openai = os.getenv("USE_OPENAI_CLASSIFIER", "false").lower() == "true"

    if not api_key or not use_openai or OpenAI is None:
        return None

    client = OpenAI(api_key=api_key)

    prompt = f"""
Classify this IT support ticket into one of:
network_issue, identity_access, hardware_issue, software_issue, security_issue, billing_issue, other

Return strict JSON with keys:
category, confidence, reasoning

Subject: {subject}
Message: {message}
Channel: {channel}
""".strip()

    try:
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=prompt,
        )

        raw = response.output_text.strip()
        data = json.loads(raw)

        category = str(data.get("category", "other")).strip()
        if category not in CATEGORY_ORDER:
            category = "other"

        confidence = float(data.get("confidence", 0.75))
        reasoning = str(data.get("reasoning", "AI classification completed."))

        return {
            "category": category,
            "confidence": round(max(0.0, min(confidence, 0.99)), 2),
            "reasoning": reasoning,
        }
    except Exception as exc:
        logger.warning("OpenAI classification failed, falling back to rules: %s", exc)
        return None


def classify_ticket(subject: str, message: str, channel: str = "web") -> Dict[str, object]:
    """
    Classify an IT support ticket.

    Returns:
        {
            "category": str,
            "confidence": float,
            "reasoning": str,
            "processing_time_ms": int
        }
    """
    start = time.perf_counter()

    if not subject or not subject.strip():
        raise ValueError("Ticket subject is required.")
    if not message or not message.strip():
        raise ValueError("Ticket message is required.")

    subject = subject.strip()
    message = message.strip()
    channel = channel.strip().lower() if channel else "web"

    classified = _openai_classification(subject, message, channel)

    if classified is None:
        classified = _rule_based_classification(subject, message)

    elapsed_ms = int((time.perf_counter() - start) * 1000)

    return {
        "category": classified["category"],
        "confidence": classified["confidence"],
        "reasoning": classified["reasoning"],
        "processing_time_ms": elapsed_ms,
    }
