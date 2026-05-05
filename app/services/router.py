from __future__ import annotations

from app.utils.logging import get_logger

logger = get_logger(__name__)

QUEUE_MAP = {
    "security_issue": "security",
    "network_issue": "tier2/network",
    "identity_access": "tier1/helpdesk",
    "hardware_issue": "tier2/hardware",
    "software_issue": "tier1/helpdesk",
    "billing_issue": "billing",
    "other": "tier1/helpdesk",
}


def assign_queue(category: str, priority: str) -> str:
    """
    Assign the ticket to the correct support queue.
    """
    base_queue = QUEUE_MAP.get(category, "tier1/helpdesk")

    if priority == "critical" and category != "security_issue":
        return "tier2/escalation"

    return base_queue
