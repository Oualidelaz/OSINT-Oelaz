import asyncio
from home.global_config import Colors
from app.connection.platforms import PLATFORMS
from app.connection.tracker import track_username

async def main(username: str) -> None:
    colors = Colors()

    results = await track_username(
        username=username,
        platforms=PLATFORMS
    )


    for result in results:
        status_code = result["status_code"]

        if status_code == 200:
            color = colors.LIGHT_GREEN
            symbol = "[+]"

        elif status_code == 404:
            color = colors.LIGHT_RED
            symbol = "[-]"

        elif status_code in (401, 403):
            color = colors.YELLOW
            symbol = "[!]"

        elif status_code == 429:
            color = colors.YELLOW
            symbol = "[!]"

        elif status_code is not None and 300 <= status_code < 400:
            color = colors.LIGHT_CYAN
            symbol = "[>]"

        elif status_code is not None and 500 <= status_code < 600:
            color = colors.LIGHT_PURPLE
            symbol = "[!]"

        else:
            color = colors.LIGHT_GRAY
            symbol = "[?]"

        print()
        print(f"{color}{symbol} Platform: {result['platform']}{colors.END}")
        print(f"{color}    Status: {result['status']}{colors.END}")
        print(f"{color}    HTTP Status: {status_code}{colors.END}")
        print(f"{color}    Profile URL: {result['profile_url']}{colors.END}")



    print(
        f"\n{colors.RED}[!]{colors.END} {colors.YELLOW}Warning{colors.END}: Some platforms may block automated requests,\n"
        "    return misleading status codes, or apply rate limits.\n"
        "    Treat every result as an investigative lead and verify it manually."
    )
    print()
    print(
        f"\n{colors.RED}[!]{colors.END} {colors.YELLOW}Identity Notice{colors.END}: Having the same username on two platforms\n"
        "    does not prove that the two accounts belong to the same person."
    )

def sc_username(username: str):
    asyncio.run(main(username))
