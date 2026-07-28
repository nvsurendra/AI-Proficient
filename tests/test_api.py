from __future__ import annotations

from fastapi.testclient import TestClient


def test_health_endpoint(client: TestClient) -> None:
    resp = client.get("/api/v1/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["db_ok"] is True


def test_create_resolve_stats_flow(client: TestClient) -> None:
    created = client.post(
        "/api/v1/links",
        json={"original_url": "https://example.com/docs", "created_by": "qa"},
    )
    assert created.status_code == 201
    code = created.json()["short_code"]

    redirect = client.get(f"/{code}", follow_redirects=False)
    assert redirect.status_code == 307
    assert redirect.headers["location"] == "https://example.com/docs"

    stats = client.get(f"/api/v1/links/{code}/stats")
    assert stats.status_code == 200
    body = stats.json()
    assert body["total_clicks"] == 1


def test_idempotent_create_same_user_url(client: TestClient) -> None:
    payload = {"original_url": "https://example.com/idempotent", "created_by": "owner-a"}

    first = client.post("/api/v1/links", json=payload)
    second = client.post("/api/v1/links", json=payload)

    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["short_code"] == second.json()["short_code"]
    assert second.json()["already_exists"] is True


def test_alias_conflict_returns_409(client: TestClient) -> None:
    first = client.post(
        "/api/v1/links",
        json={"original_url": "https://example.com/a", "custom_alias": "alias123"},
    )
    second = client.post(
        "/api/v1/links",
        json={"original_url": "https://example.com/b", "custom_alias": "alias123"},
    )

    assert first.status_code == 201
    assert second.status_code == 409


def test_rate_limit_returns_429(client: TestClient) -> None:
    one = client.post("/api/v1/links", json={"original_url": "https://example.com/1"})
    two = client.post("/api/v1/links", json={"original_url": "https://example.com/2"})
    three = client.post("/api/v1/links", json={"original_url": "https://example.com/3"})
    four = client.post("/api/v1/links", json={"original_url": "https://example.com/4"})

    assert one.status_code == 201
    assert two.status_code == 201
    assert three.status_code == 201
    assert four.status_code == 429


def test_deactivate_link_blocks_resolution(client: TestClient) -> None:
    created = client.post("/api/v1/links", json={"original_url": "https://example.com/kill"})
    code = created.json()["short_code"]

    deact = client.delete(f"/api/v1/links/{code}")
    assert deact.status_code == 200
    assert deact.json()["deactivated"] is True

    resolve = client.get(f"/{code}", follow_redirects=False)
    assert resolve.status_code == 404
