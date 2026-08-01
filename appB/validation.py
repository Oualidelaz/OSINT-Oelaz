import ipaddress
from home.global_config import Colors


def ip_validation(ip_addr):
    colors = Colors()

    if not ip_addr:
        print(f"\n{colors.RED}[!] IP address cannot be empty. Please enter a valid IP.{colors.END}")
        return False

    try:
        address = ipaddress.ip_address(ip_addr)
    except ValueError:
        print(f"\n{colors.RED}[-] Invalid IP address: {ip_addr}{colors.END}")
        return False

    
    if address.is_unspecified:
        print(
            f"\n{colors.YELLOW}[!] "
            f"Unspecified IP addresses are not supported: {address}"
            f"{colors.END}"
        )
        return False

    if address.is_loopback:
        print(
            f"\n{colors.YELLOW}[!] "
            f"Loopback IP addresses are not valid OSINT targets: {address}"
            f"{colors.END}"
        )
        return False
    
    if address.is_multicast:
        print(
            f"\n{colors.YELLOW}[!] "
            f"Multicast IP addresses are not supported: {address}"
            f"{colors.END}"
        )
        return False

    if address.is_link_local:
        print(
            f"\n{colors.YELLOW}[!] "
            f"Link-local IP addresses are not publicly reachable: {address}"
            f"{colors.END}"
        )
        return False

    if address.is_reserved:
        print(
            f"\n{colors.YELLOW}[!] "
            f"Reserved IP addresses are not supported: {address}"
            f"{colors.END}"
        )
        return False
    
    if not address.is_global:
        print(
            f"\n{colors.YELLOW}[!] "
            f"The IP address is valid but is not globally reachable: {address}"
            f"{colors.END}"
        )
        return False

    print(
        f"\n{colors.GREEN}[+] "
        f"Valid public IPv{address.version} address: {address}"
        f"{colors.END}"
    )

    return True