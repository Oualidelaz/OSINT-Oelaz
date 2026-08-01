import httpx

def create_http_client() -> httpx.AsyncClient:
    timeout = httpx.Timeout(
        connect=5.0,
        read=10.0,
        write=10.0,
        pool=5.0,
    )

    limits = httpx.Limits(
        max_connections=10,
        max_keepalive_connections=5,
        keepalive_expiry=10.0,
    )

    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
    }

    return httpx.AsyncClient(
        timeout=timeout,
        limits=limits,
        headers=headers,
        follow_redirects=False,
        verify=True,
        trust_env=False,
    )
