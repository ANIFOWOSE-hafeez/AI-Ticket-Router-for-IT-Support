# Architecture

## Flow
Ticket Source → Webhook Receiver → Validation → AI Classification → Priority Engine → Routing Engine → Zendesk / Queue

## Core modules
- `classifier.py` handles ticket category detection
- `priority.py` determines urgency
- `router.py` assigns the support queue
- `client.py` handles Zendesk integration

## Notes
The project runs in dry-run mode when Zendesk credentials are not configured.
