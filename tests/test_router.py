from app.services.router import assign_queue


def test_router_network():
    assert assign_queue("network_issue", "high") == "tier2/network"


def test_router_security():
    assert assign_queue("security_issue", "critical") == "security"


def test_router_critical_escalation():
    assert assign_queue("hardware_issue", "critical") == "tier2/escalation"
