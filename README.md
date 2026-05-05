# AI Ticket Router for IT Support

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production%20API-009688)
![OpenAI](https://img.shields.io/badge/OpenAI-NLP-orange)
![Zendesk](https://img.shields.io/badge/Zendesk-Integration-03363D)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An AI-powered ticket classification and routing system that automatically analyzes incoming support requests, assigns priority, and routes them to the correct support tier before a human touches the ticket.

---

## Overview

**AI Ticket Router for IT Support** solves one of the most common bottlenecks in support operations: manual ticket triage.

In fast-growing teams, support requests often arrive from multiple channels such as web forms, email, chat, or internal tools. Without automation, the help desk team must manually read every request, decide the category, assign priority, and forward it to the right queue. That process slows down response time, creates routing mistakes, and wastes engineering hours.

This project uses **AI + NLP + API automation** to classify each ticket, determine urgency, and route it automatically to the correct team.

The result is a faster, cleaner, and more scalable support workflow.

---

## Problem

The support team was overwhelmed by unstructured tickets arriving from multiple channels.

Manual triage caused:

* slower first response times
* misrouted tickets
* SLA breaches
* repeated engineer interruptions
* wasted time on repetitive sorting work

For a startup, this kind of inefficiency quickly becomes expensive because every delayed ticket affects user experience, internal productivity, and team morale.

---

## Solution

I built an AI-powered ticket classification engine that:

* reads incoming ticket subject and message
* detects the issue category using NLP
* estimates ticket urgency
* assigns a priority level
* routes the ticket to the right support queue automatically

The system removes first-pass manual triage and ensures tickets are handled faster and more consistently.

---

## Key Features

* Automatic ticket classification
* Priority detection and scoring
* Intelligent routing to support tiers
* Webhook-based ticket intake
* Zendesk API integration
* NLP-driven text analysis
* Structured JSON responses for downstream systems
* Logging for audit, debugging, and observability
* Dashboard-ready metrics for monitoring performance

---

## Tech Stack

* **Python** for backend logic and automation
* **FastAPI** for the API layer
* **OpenAI API** for NLP classification and intent detection
* **Zendesk API** for ticket integration
* **Webhooks** for real-time ticket intake
* **PostgreSQL** for storing tickets, classifications, and metrics
* **Docker** for deployment consistency

---

## Architecture

```text
Ticket Source (Web / Email / Chat)
        ↓
Webhook Receiver
        ↓
Normalization Layer
        ↓
AI Classification Engine
        ↓
Priority Scoring Module
        ↓
Routing Logic
        ↓
Zendesk / Support Queue
        ↓
Logs + Metrics Dashboard
```

---

## How It Works

1. A user submits a support ticket.
2. The webhook receives the ticket payload.
3. The system normalizes and validates the input.
4. The AI classifies the ticket category.
5. The model estimates urgency and assigns priority.
6. The routing engine sends the ticket to the correct queue.
7. A log entry is created for auditing and reporting.
8. Metrics are displayed in the dashboard.

---

## Demo Logs

The logs below are **simulated production-style logs** for portfolio demonstration.

### Ticket Intake Log

```log
2026-05-05 08:14:02 INFO  webhook.receiver      - Incoming ticket received from /api/tickets/classify
2026-05-05 08:14:02 INFO  ticket.validator       - Payload validated successfully
2026-05-05 08:14:03 INFO  nlp.classifier         - Subject parsed: "VPN not working"
2026-05-05 08:14:03 INFO  nlp.classifier         - Category predicted: network_issue
2026-05-05 08:14:03 INFO  priority.engine       - Priority assigned: high
2026-05-05 08:14:03 INFO  routing.engine         - Assigned queue: tier2/network
2026-05-05 08:14:03 INFO  zendesk.sync           - Ticket pushed to Zendesk successfully
2026-05-05 08:14:03 INFO  metrics.tracker        - Processing time: 428ms
```

### Security / Access Issue Log

```log
2026-05-05 09:21:17 INFO  webhook.receiver      - Incoming ticket received from /api/tickets/classify
2026-05-05 09:21:17 INFO  ticket.validator       - Payload validated successfully
2026-05-05 09:21:18 INFO  nlp.classifier         - Subject parsed: "Cannot access email account"
2026-05-05 09:21:18 INFO  nlp.classifier         - Category predicted: identity_access
2026-05-05 09:21:18 INFO  priority.engine       - Priority assigned: medium
2026-05-05 09:21:18 INFO  routing.engine         - Assigned queue: tier1/helpdesk
2026-05-05 09:21:18 INFO  zendesk.sync           - Ticket pushed to Zendesk successfully
2026-05-05 09:21:18 INFO  metrics.tracker        - Processing time: 391ms
```

### Hardware Issue Log

```log
2026-05-05 10:07:45 INFO  webhook.receiver      - Incoming ticket received from /api/tickets/classify
2026-05-05 10:07:45 INFO  ticket.validator       - Payload validated successfully
2026-05-05 10:07:46 INFO  nlp.classifier         - Subject parsed: "Laptop keeps shutting down"
2026-05-05 10:07:46 INFO  nlp.classifier         - Category predicted: hardware_issue
2026-05-05 10:07:46 INFO  priority.engine       - Priority assigned: high
2026-05-05 10:07:46 INFO  routing.engine         - Assigned queue: tier2/hardware
2026-05-05 10:07:46 INFO  zendesk.sync           - Ticket pushed to Zendesk successfully
2026-05-05 10:07:46 INFO  metrics.tracker        - Processing time: 512ms
```

---

## Dashboard

The dashboard gives support and engineering teams visibility into classification performance and ticket flow.

### Suggested Dashboard Widgets

* Total tickets processed today
* Average first-response time
* Auto-classification accuracy
* Tickets routed by queue
* Top issue categories
* SLA risk count
* Processing latency
* Manual triage avoided

### Example Dashboard Snapshot

```text
AI Ticket Router Dashboard
-------------------------------------------------
Tickets Processed Today        524
Auto-Classified Accuracy       96.8%
Average Processing Time         0.43s
Manual Triage Avoided           417 tickets
First-Response Time Reduction   40%
SLA Breaches                    0

Top Categories:
- network_issue
- identity_access
- hardware_issue
- billing_issue
- software_bug

Queue Distribution:
- tier1/helpdesk        42%
- tier2/network         23%
- tier2/hardware        18%
- security              9%
- billing               8%
-------------------------------------------------
```

### Dashboard Views to Include in Your Repo

* Overview page
* Ticket classification chart
* Queue routing chart
* SLA status panel
* Processing latency graph
* Audit log table

---

## API Example

### Request

```http
POST /api/tickets/classify
Authorization: Bearer ***
Content-Type: application/json
```

### Payload

```json
{
  "subject": "VPN not working",
  "message": "I cannot connect to the company VPN from home.",
  "channel": "email",
  "priority": "auto"
}
```

### Response

```json
{
  "ticket_id": "TCK-10482",
  "category": "network_issue",
  "priority": "high",
  "assigned_team": "tier2_network",
  "confidence": 0.97,
  "processing_time_ms": 428,
  "status": "routed"
}
```

---

## Example Classification Rules

| Input Issue               | Predicted Category |          Queue | Priority |
| ------------------------- | ------------------ | -------------: | -------: |
| VPN not working           | network_issue      |  tier2/network |     high |
| Cannot log in             | identity_access    | tier1/helpdesk |   medium |
| Laptop overheating        | hardware_issue     | tier2/hardware |     high |
| Software install failed   | software_issue     | tier1/helpdesk |   medium |
| Suspicious email received | security_issue     |       security |     high |

---

## Performance Metrics

These are realistic portfolio metrics you can present as **demo results**.

* **40% reduction** in first-response time
* **2+ engineer-hours saved daily**
* **96%+ classification accuracy** on test tickets
* **< 500ms average processing time** per ticket
* **0 manual triage required** for standard requests

> Note: If your project is still a demo, label metrics as **simulated** or **benchmark results** in interviews and documentation.

---

## Folder Structure

```bash
.
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── main.py
├── integrations/
│   └── zendesk/
├── logs/
├── dashboard/
├── tests/
├── assets/
│   ├── demo.gif
│   ├── dashboard.png
│   └── logs.png
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

* Python 3.10+
* PostgreSQL
* OpenAI API key
* Zendesk API credentials

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-ticket-router.git
cd ai-ticket-router

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
ZENDESK_API_KEY=your_zendesk_key
DATABASE_URL=postgresql://user:password@localhost:5432/tickets
WEBHOOK_SECRET=your_secret
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

### Run Tests

```bash
pytest
```

---

## Testing Strategy

* Unit tests for classification logic
* Integration tests for Zendesk API sync
* Webhook payload validation tests
* Routing rule tests
* Performance tests for processing latency

### Example Test Cases

* Ticket with network keywords routes to tier2/network
* Empty payload returns validation error
* High urgency security issue routes to security queue
* Duplicate ticket is detected and logged

---

## Observability and Logging

This project is designed with production-style observability in mind.

### Logged Events

* ticket received
* payload validated
* classification completed
* priority assigned
* queue selected
* Zendesk sync completed
* processing latency captured
* errors and retries recorded

### Why This Matters

Logs make it easier to:

* debug misclassifications
* audit routing decisions
* measure support performance
* identify bottlenecks
* prove reliability to stakeholders

---

## Security Considerations

* API requests should be authenticated
* Secrets must be stored in environment variables
* Webhook payloads should be validated
* Logs should not expose sensitive user data
* Rate limiting should be enabled for public endpoints

---

## Future Improvements

* Multilingual classification
* Confidence thresholding for human review
* Slack / Microsoft Teams alerts
* Support analytics dashboard
* Fine-tuned custom NLP model
* Duplicate ticket detection
* SLA prediction engine

---

---

## Disclaimer

This project is a portfolio/demo system. Any metrics, logs, and dashboard numbers shown in this README are presented as **simulated production-style examples** for demonstration purposes unless backed by live data in your deployed implementation.

---

## License

MIT

```
```
