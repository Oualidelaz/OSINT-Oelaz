from home.global_config import Colors
import re

MIN_USERNAME_LENGTH = 1
MAX_USERNAME_LENGTH = 100
FORBIDDEN_URL_CHARACTERS = re.compile(r'[/\\?#%&=\x00-\x1F\x7F]')

def username_validation(username):
    colors = Colors()
    if not username:
        print(f"\n{colors.RED}[!] Username cannot be empty. Please enter a valid username.{colors.END}")
        return False

    if len(username) > MAX_USERNAME_LENGTH or len(username) < MIN_USERNAME_LENGTH:
        print(
            f"\n{colors.RED}[!] Username length must be between "
            f"{MIN_USERNAME_LENGTH} and {MAX_USERNAME_LENGTH} characters.{colors.END}"
        )
        return False 
    
    if username.startswith("@"):
        print(f"\n{colors.RED}[!] Please enter the username without the '@' symbol.{colors.END}")
        return False

    if any(character.isspace() for character in username):
        print(f"\n{colors.RED}[!] Username cannot contain spaces or whitespace characters.{colors.END}")
        return False
    
    if any(ord(character) < 32 or ord(character) == 127 for character in username):
        print(f"\n{colors.RED}[!] Username contains invalid control characters.{colors.END}")
        return False
    
    if username.lower().startswith(("http://", "https://", "www.")):
        print(f"\n{colors.RED}[!] Enter only the username, not a complete URL.{colors.END}")
        return False

    if FORBIDDEN_URL_CHARACTERS.search(username):
        print(f"\n{colors.RED}[!] Username contains URL-reserved or invalid characters.{colors.END}")
        return False

    return True