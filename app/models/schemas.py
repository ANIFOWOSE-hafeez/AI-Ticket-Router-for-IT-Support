from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TicketClassifyRequest(BaseModel):
    subject: str = Field(..., min_length=3, max_length=200)
    message: str = Field(..., min_length=3, max_length=4000)
    channel: str = Field(default="web", min_length=2, max_length=50)
    priority: str = Field(default="auto", min_length=2, max_length=20)
    requester_email: Optional[str] = Field(default=None, max_length=200)


class TicketClassifyResponse(BaseModel):
    ticket_id: str
    category: str
    priority: str
    assigned_team: str
    confidence: float
    processing_time_ms: int
    status: str
    reasoning: str
    received_at: datetime
