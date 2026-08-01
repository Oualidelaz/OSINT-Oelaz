from home.global_config import Colors

def number_display(fields: list[tuple[str, object]]):
    colors = Colors()
    print(
        f"{colors.LIGHT_GREEN}[+] "
        f"Phone number information successfully retrieved"
        f"{colors.END}"
    )

    print(
        f"{colors.CYAN}"
        f"{'=' * 55}\n"
        f"              PHONE NUMBER REPORT\n"
        f"{'=' * 55}"
        f"{colors.END}"
    )

    for label, value in fields:
        print(
            f"{colors.LIGHT_BLUE}{label:<22}"
            f"{colors.END}: "
            f"{colors.LIGHT_WHITE}{value}{colors.END}"
        )

    print(f"{colors.CYAN}{'=' * 55}{colors.END}")
