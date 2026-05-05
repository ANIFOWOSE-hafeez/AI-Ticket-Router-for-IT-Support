from __future__ import annotations

import os
from typing import Dict, Any

from app.utils.logging import get_logger

logger = get_logger(__name__)


class ZendeskClient:
    """
    Lightweight Zendesk client.

    Works in dry-run mode when credentials are not configured,
    so the project remains fully runnable locally.
    """

    def __init__(self):
        self.subdomain = os.getenv("ZENDESK_SUBDOMAIN")
        self.email = os.getenv("ZENDESK_EMAIL")
        self.api_token = os.getenv("ZENDESK_API_TOKEN")
        self.enabled = bool(self.subdomain and self.email and self.api_token)

    def create_ticket(
        self,
        ticket_id: str,
        subject: str,
        message: str,
        category: str,
        priority: str,
        assigned_team: str,
        channel: str,
    ) -> Dict[str, Any]:
        payload = {
            "ticket_id": ticket_id,
            "subject": subject,
            "message": message,
            "category": category,
            "priority": priority,
            "assigned_team": assigned_team,
            "channel": channel,
        }

        if not self.enabled:
            logger.info("Zendesk dry-run mode enabled. Ticket not pushed externally.")
            return {
                "success": True,
                "mode": "dry_run",
                "payload": payload,
            }

        try:
            import requests

            url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets.json"
            auth = (f"{self.email}/token", self.api_token)
            headers = {"Content-Type": "application/json"}

            body = {
                "ticket": {
                    "subject": subject,
                    "comment": {"body": message},
                    "priority": priority,
                    "tags": [category, assigned_team, channel],
                }
            }

            response = requests.post(url, json=body, auth=auth, headers=headers, timeout=15)
            response.raise_for_status()

            logger.info("Zendesk ticket created successfully.")
            return {
                "success": True,
                "mode": "live",
                "zendesk_status_code": response.status_code,
                "payload": payload,
            }

        except Exception as exc:
            logger.exception("Zendesk ticket creation failed.")
            return {
                "success": False,
                "mode": "live",
                "error": str(exc),
                "payload": payload,
            }
