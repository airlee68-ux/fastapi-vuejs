def get_auth_header(client):
    """테스트용 사용자를 생성하고 인증 헤더를 반환합니다."""
    client.post(
        "/auth/register",
        json={"username": "writer", "password": "test1234"},
    )
    resp = client.post(
        "/auth/login",
        data={"username": "writer", "password": "test1234"},
    )
    token = resp.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
