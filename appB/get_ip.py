from home.global_config import Colors
import socket
import ipaddress
import requests

colors = Colors()


def show_your_public_ip() -> None:
    try:
        hostname = socket.gethostname()

        response = requests.get(
            "https://api.ipify.org",
            timeout=5
        )
        response.raise_for_status() # checks whether the HTTP request failed

        external_ip = response.text.strip()

        if not external_ip:
            print(
                f"{colors.YELLOW}[!] "
                f"The IP service returned an empty response."
                f"{colors.END}"
            )
            return

        # check the IP address is valid
        ipaddress.ip_address(external_ip)

        print(
            f"\n{colors.LIGHT_GREEN}[+] "
            f"Network Intelligence | Asset: {hostname} | "
            f"External IP: {external_ip}"
            f"{colors.END}"
        )

    except requests.exceptions.Timeout:
        print(
            f"{colors.LIGHT_RED}[-] "
            f"Error: The request timed out."
            f"{colors.END}"
        )

    except requests.exceptions.ConnectionError:
        print(
            f"{colors.LIGHT_RED}[-] "
            f"Error: Unable to connect to the IP service."
            f"{colors.END}"
        )

    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code

        print(
            f"{colors.LIGHT_RED}[-] "
            f"Error: The IP service returned HTTP status {status_code}."
            f"{colors.END}"
        )

    except requests.exceptions.RequestException as error:
        print(
            f"{colors.LIGHT_RED}[-] "
            f"Error: The request failed: {error}"
            f"{colors.END}"
        )

    except ValueError:
        print(
            f"{colors.YELLOW}[!] "
            f"The IP service returned an invalid IP address."
            f"{colors.END}"
        )

    except OSError as error:
        print(
            f"{colors.LIGHT_RED}[-] "
            f"Error: Unable to retrieve the hostname: {error}"
            f"{colors.END}"
        )
