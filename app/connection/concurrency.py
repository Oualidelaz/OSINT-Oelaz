import asyncio
import httpx
from app.connection.platform_checker import check_platform

async def limited_check(
    semaphore: asyncio.Semaphore,
    client: httpx.AsyncClient,
    platform: dict,
    username: str,
) -> dict:
    async with semaphore:
        return await check_platform(
            client=client,
            platform=platform,
            username=username,
        )
