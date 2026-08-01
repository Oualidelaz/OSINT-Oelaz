import asyncio
from app.connection.concurrency import limited_check
from app.connection.config import MAX_CONCURRENT_REQUESTS
from app.connection.http_client import create_http_client

async def track_username(
    username: str,
    platforms: list[dict],
) -> list[dict]:

    semaphore = asyncio.Semaphore(
        MAX_CONCURRENT_REQUESTS
    )

    async with create_http_client() as client:  # create a client http
        tasks = [
            limited_check(
                semaphore=semaphore,
                client=client,
                platform=platform,
                username=username
            )

            for platform in platforms
        ]

        results = await asyncio.gather(*tasks)

    return results
