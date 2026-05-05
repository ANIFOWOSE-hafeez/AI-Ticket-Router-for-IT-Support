from __future__ import annotations

from app.models.schemas import TicketClassifyRequest


def _clean_text(text: str) -> str:
    return " ".join(text.strip().split())


def normalize_ticket_request(payload: TicketClassifyRequest) -> TicketClassifyRequest:
    """
    Normalize and validate incoming ticket data.
    """
    data = payload.model_dump() if hasattr(payload, "model_dump") else payload.dict()

    subject = _clean_text(str(data.get("subject", "")))
    message = _clean_text(str(data.get("message", "")))
    channel = _clean_text(str(data.get("channel", "web"))).lower()
    priority = _clean_text(str(data.get("priority", "auto"))).lower()
    requester_email = data.get("requester_email")

    if len(subject) < 3:
        raise ValueError("Subject must be at least 3 characters long.")
    if len(message) < 3:
        raise ValueError("Message must be at least 3 characters long.")

    return TicketClassifyRequest(
        subject=subject,
        message=message,
        channel=channel,
        priority=priority,
        requester_email=requester_email,
    )
