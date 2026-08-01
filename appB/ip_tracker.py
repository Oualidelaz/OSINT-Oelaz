import ipaddress
from statistics import correlation
from httpx import Request
import requests
from home.global_config import Colors
import json


def extract_ip_info(ip_addr):

    try:
        colors = Colors()
        address = ipaddress.ip_address(ip_addr)

        response = requests.get(
            f"https://ipinfo.io/{ip_addr}/json",
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            print(
                f"\n{colors.RED}[-] "
                f"IPinfo returned an unexpected data format."
                f"{colors.END}"
            )
            return False

        if "error" in data:
            error_data = data["error"]
        
            if isinstance(error_data, dict):
                error_message = error_data.get("message", "Unknown API error")
            else:
                error_message = str(error_data)
            

            print(
                f"\n{colors.RED}[-] IPinfo error: "
                f"{error_message}{colors.END}"
            )

            return False

        latitude = "N/A"
        longitude = "N/A"

        if "loc" in data:
            coordinates = data.get("loc", "")
        else:
            coordinates = "N/A"
        
        if coordinates and "," in coordinates:
            latitude, longitude = coordinates.split(',', maxsplit=1)

        organization = data.get("org", "")

        if organization:
            asn, separator, provider = organization.partition(" ")
        
            if not separator:
                provider = "N/A"
        
        else:
            asn = "N/A"
            provider = "N/A"

        
        hostname = data.get("hostname") or "N/A"

        fields = [
            ("IP Address", data.get("ip")),
            ("IP Version", f"IPv{address.version}"),
            ("Hostname", hostname),
            ("City", data.get("city", "N/A")),
            ("Region", data.get("region", "N/A")),
            ("Country Code", data.get("country", "N/A")),
            ("Postal Code", data.get("postal", "N/A")),
            ("Latitude", latitude),
            ("Longitude", longitude),
            ("Timezone", data.get("timezone", "N/A")),
            ("ASN", asn),
            ("Organization", provider),
            ("Anycast", data.get("anycast", "N/A")),
            ("Bogon", data.get("bogon", "N/A")),
        ]

        print(
            f"\n{colors.LIGHT_GREEN}[+] "
            f"IP intelligence successfully retrieved"
            f"{colors.END}"
        )

        print(
            f"{colors.CYAN}"
            f"{'=' * 55}\n"
            f"                 IP INTELLIGENCE REPORT\n"
            f"{'=' * 55}"
            f"{colors.END}"
        )

        for label, value in fields:
            print(
                f"{colors.LIGHT_BLUE}{label:<18}"
                f"{colors.END}: "
                f"{colors.LIGHT_WHITE}{value}{colors.END}"
            )

        print(f"{colors.CYAN}{'=' * 55}{colors.END}")

        return True

    except ValueError:
        print(
            f"\n{colors.RED}[-] Invalid IPv4 or IPv6 address: "
            f"{ip_addr}{colors.END}"
        )
        return False

    except requests.exceptions.Timeout:
        print(
            f"\n{colors.RED}[-] The IP intelligence request "
            f"timed out.{colors.END}"
        )
        return False

    except requests.exceptions.ConnectionError:
        print(
            f"\n{colors.RED}[-] Unable to connect to "
            f"IPinfo.{colors.END}"
        )
        return False
    
    except requests.exceptions.HTTPError as error:
        status_code = (
            error.response.status_code
            if error.response is not None
            else "Unknown"
        )

        print(
            f"\n{colors.RED}[-] IPinfo returned HTTP status "
            f"{status_code}.{colors.END}"
        )
        return False

    except requests.exceptions.JSONDecodeError:
        print(
            f"\n{colors.RED}[-] IPinfo returned invalid "
            f"JSON data.{colors.END}"
        )
        return False

    except requests.exceptions.RequestException as error:
        print(
            f"\n{colors.RED}[-] IP intelligence request failed: "
            f"{error}{colors.END}"
        )
        return False