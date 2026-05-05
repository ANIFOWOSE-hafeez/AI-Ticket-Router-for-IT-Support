from __future__ import annotations

from app.utils.logging import get_logger

logger = get_logger(__name__)

CRITICAL_TERMS = [
    "outage",
    "down",
    "breach",
    "compromised",
    "ransomware",
    "urgent",
    "critical",
    "data loss",
]

HIGH_TERMS = [
    "vpn",
    "cannot access",
    "locked out",
    "overheating",
    "shutdown",
    "error",
    "failed",
    "broken",
]

MEDIUM_TERMS = [
    "slow",
    "issue",
    "problem",
    "help",
    "question",
    "request",
]


def determine_priority(category: str, text: str) -> str:
    """
    Determine priority using category and ticket text.
    """
    normalized = " ".join(text.lower().split())

    if category == "security_issue":
        return "critical"

    if any(term in normalized for term in CRITICAL_TERMS):
        return "critical"

    if category in {"network_issue", "hardware_issue"}:
        if any(term in normalized for term in HIGH_TERMS):
            return "high"
        return "high"

    if category in {"identity_access", "software_issue", "billing_issue"}:
        if any(term in normalized for term in HIGH_TERMS):
            return "high"
        if any(term in normalized for term in MEDIUM_TERMS):
            return "medium"
        return "medium"

    return "low"
