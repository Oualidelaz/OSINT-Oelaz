from urllib.parse import quote

def build_profile_url(
    platform: dict,
    username: str,
) -> str:

    encoded_username = quote(username, safe="")

    return platform["url"].format(username=encoded_username)
