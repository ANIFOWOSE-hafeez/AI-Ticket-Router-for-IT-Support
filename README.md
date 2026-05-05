# AI Ticket Router for IT Support

An AI-powered ticket classification system that automatically analyzes incoming support requests, assigns priority, and routes them to the correct team or tier.

## Overview

This project was built to solve a common IT support problem: tickets arriving from multiple channels without clear categorization. Instead of relying on manual triage, the system uses NLP and AI to classify each ticket and route it automatically.

The result is faster response times, better ticket handling consistency, and less time wasted by support engineers on repetitive sorting tasks.

## Problem

The support team was overwhelmed by unclassified tickets coming in from different sources.  
Manual triage caused:

- delays in first response
- misdirected tickets
- SLA breaches
- wasted engineering time

## Solution

I built an AI-powered ticket routing engine that:

- reads incoming ticket text
- detects the issue category
- estimates urgency
- assigns priority
- routes the ticket to the right support queue

This allows the support team to focus on solving issues instead of sorting them.

## Features

- Automatic ticket classification
- Priority detection
- Intelligent routing to support tiers
- Webhook-based ticket intake
- Zendesk integration
- NLP-driven text analysis
- Logging for audit and debugging

## Tech Stack

- Python
- OpenAI API
- Zendesk API
- Webhooks
- NLP

## Impact

- Reduced average first-response time by 40%
- Eliminated manual triage overhead
- Saved 2+ engineer-hours per day
- Improved consistency in ticket handling

## Example Flow

1. A user submits a support ticket.
2. The system reads the ticket subject and description.
3. The AI classifies the issue.
4. The ticket is assigned a priority.
5. The ticket is routed to the correct queue automatically.

## Example Request
```http
POST /api/tickets/classify
Authorization: Bearer ***

{
  "subject": "VPN not working",
  "priority": "auto",
  "route": "tier2/network"
}

Future Improvements
Add multilingual support
Improve confidence scoring
Add Slack/Teams alerts
Build a dashboard for ticket analytics
Support more help desk platforms
```http
POST /api/tickets/classify
Authorization: Bearer ***
