from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from app.models.schemas import TicketClassifyRequest, TicketClassifyResponse
from app.services.classifier import classify_ticket
from app.services.priority import determine_priority
from app.services.router import assign_queue
from app.integrations.zendesk.client import ZendeskClient
from app.utils.logging import get_logger
from app.utils.validators import normalize_ticket_request

router = APIRouter()
logger = get_logger(__name__)
zendesk_client = ZendeskClient()


@router.post(
    "/tickets/classify",
    response_model=TicketClassifyResponse,
    status_code=status.HTTP_200_OK,
)
def classify_incoming_ticket(payload: TicketClassifyRequest):
    try:
        clean_payload = normalize_ticket_request(payload)

        classification = classify_ticket(
            subject=clean_payload.subject,
            message=clean_payload.message,
            channel=clean_payload.channel,
        )

        priority = determine_priority(
            category=classification["category"],
            text=f"{clean_payload.subject} {clean_payload.message}",
        )

        assigned_team = assign_queue(
            category=classification["category"],
            priority=priority,
        )

        ticket_id = f"TCK-{uuid4().hex[:8].upper()}"
        received_at = datetime.now(timezone.utc)

        zendesk_result = zendesk_client.create_ticket(
            ticket_id=ticket_id,
            subject=clean_payload.subject,
            message=clean_payload.message,
            category=classification["category"],
            priority=priority,
            assigned_team=assigned_team,
            channel=clean_payload.channel,
        )

        response = TicketClassifyResponse(
            ticket_id=ticket_id,
            category=classification["category"],
            priority=priority,
            assigned_team=assigned_team,
            confidence=classification["confidence"],
            processing_time_ms=classification["processing_time_ms"],
            status="routed" if zendesk_result.get("success", True) else "queued",
            reasoning=classification["reasoning"],
            received_at=received_at,
        )

        return response

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Ticket classification failed")
        raise HTTPException(
            status_code=500,
            detail="Internal server error while classifying ticket.",
        ) from exc
