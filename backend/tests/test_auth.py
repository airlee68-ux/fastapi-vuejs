def test_register(client):
    resp = client.post(
        "/auth/register",
        json={
            "username": "newuser",
            "password": "pass1234",
        },
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["username"] == "newuser"
    assert "id" in body
    assert "password" not in body
