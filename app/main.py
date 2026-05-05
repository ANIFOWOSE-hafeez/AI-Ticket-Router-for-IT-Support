from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.tickets import router as tickets_router
from app.utils.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="AI Ticket Router for IT Support",
    description="AI-powered ticket classification and routing system for IT support teams.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets_router, prefix="/api", tags=["Tickets"])


@app.get("/", tags=["Health"])
def root():
    return {
        "service": "AI Ticket Router for IT Support",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "service": "ai-ticket-router",
    }
