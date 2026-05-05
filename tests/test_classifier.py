from app.services.classifier import classify_ticket


def test_classify_network_issue():
    result = classify_ticket(
        subject="VPN not working",
        message="I cannot connect to the company VPN from home.",
        channel="email",
    )
    assert result["category"] == "network_issue"
    assert 0 <= result["confidence"] <= 1


def test_classify_identity_access():
    result = classify_ticket(
        subject="Locked out of account",
        message="I forgot my password and cannot sign in.",
        channel="web",
    )
    assert result["category"] == "identity_access"


def test_classify_security_issue():
    result = classify_ticket(
        subject="Suspicious email received",
        message="This looks like phishing.",
        channel="chat",
    )
    assert result["category"] == "security_issue"
