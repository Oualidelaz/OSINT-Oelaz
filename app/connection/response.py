def classify_response(response, platform):
    status_code = response.status_code
    check_type = platform.get("check_type")

    if status_code == 429:
        return "rate_limited"
    
    if status_code in (401, 403):
        return "blocked"
    
    if status_code >= 500:
        return "platform_error"
    
    if check_type == "status_code":
        if status_code == 200:
            return "found"
        
        if status_code == 404:
            return "not_found"
        
        if 300 <= status_code < 400:
            return "redirected"
        
        return "inconclusive"

    if check_type in ("content", "content_or_status", "content_or_redirect"):
        if status_code == 404:
            return "not_found"
        
        if status_code == 200:
            return "needs_content_analysis"
        
        if 300 <= status_code < 400:
            return "needs_redirect_analysis"

        return "inconclusive"

    return "unsupported_check_type"

def unified_error(
    platform: dict,
    username: str,
    profile_url: str,
    status: str,
    message: str,
) -> dict:
    return {
        "platform": platform["name"],
        "username": username,
        "profile_url": profile_url,
        "final_url": None,
        "status": status,
        "status_code": None,
        "redirect_location": None,
        "elapsed_ms": None,
        "error": message,
    }
