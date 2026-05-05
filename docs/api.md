# API Reference

## POST /api/tickets/classify

### Request

{
  "subject": "VPN not working",
  "message": "I cannot connect to the company VPN from home.",
  "channel": "email",
  "priority": "auto"
}

### Response
{
  "ticket_id": "TCK-XXXXXXXX",
  "category": "network_issue",
  "priority": "high",
  "assigned_team": "tier2/network",
  "confidence": 0.92,
  "processing_time_ms": 120,
  "status": "routed",
  "reasoning": "Matched keywords for network_issue: vpn, connect",
  "received_at": "2026-05-05T08:14:03Z"
}

---
