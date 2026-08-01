import httpx
import time
from app.connection.response import classify_response, unified_error
from app.connection.url_builder import build_profile_url


async def check_platform(
    client: httpx.AsyncClient,
    platform: dict,
    username: str,
) -> dict:
    
    profile_url = build_profile_url(
        platform=platform,
        username=username
    )

    started_at = time.perf_counter()

    try:
        async with client.stream(
            method="GET",
            url=profile_url,
        ) as response:
            
            elapsed_ms = round(
                (time.perf_counter() - started_at) * 1000
            )

            return {
               "platform": platform["name"],
               "username": username,
               "profile_url": profile_url, 
               "final_url": str(response.url),
               "status": classify_response(response, platform=platform),
               "status_code": response.status_code,
               "redirect_location": response.headers.get("location"),
               "elapsed_ms": elapsed_ms,
               "error": None,
            }

    except httpx.TimeoutException:
        return unified_error(
            platform=platform,
            username=username,
            profile_url=profile_url,
            status="timeout",
            message = "The request exceeded the allowed timeout.",
        )

    except httpx.TooManyRedirects: # make follow_redirects=True
        return unified_error(
            platform=platform,
            username=username,
            profile_url=profile_url,
            status="redirect_error",
            message = "The platform returned too many redirects.",
        )

    except httpx.RequestError as error:
        return unified_error(
            platform=platform,
            username=username,
            profile_url=profile_url,
            status="network_error",
            message = str(error),
        )
