from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ticket_classification_api():
    response = client.post(
        "/api/tickets/classify",
        json={
            "subject": "VPN not working",
            "message": "I cannot connect to the company VPN from home.",
            "channel": "email",
            "priority": "auto",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "network_issue"
    assert data["assigned_team"] == "tier2/network"
    assert data["status"] in ["routed", "queued"]
    assert "ticket_id" in data
