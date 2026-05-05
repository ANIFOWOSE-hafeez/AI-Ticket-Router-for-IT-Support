# Architecture
<img width="1024" height="1536" alt="AI Ticket Router Architecture" src="https://github.com/user-attachments/assets/5448daf7-4831-4430-b785-5506eb5f325e" />

## Flow
Ticket Source → Webhook Receiver → Validation → AI Classification → Priority Engine → Routing Engine → Zendesk / Queue

## Core modules
- `classifier.py` handles ticket category detection
- `priority.py` determines urgency
- `router.py` assigns the support queue
- `client.py` handles Zendesk integration

## Notes
The project runs in dry-run mode when Zendesk credentials are not configured.
