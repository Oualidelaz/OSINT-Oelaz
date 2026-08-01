import phonenumbers
from phonenumbers import NumberParseException
from home.global_config import Colors



def number_validation(phone_number: str):
    colors = Colors()

    if not phone_number:
        print(
            f"\n{colors.RED}"
            "[!] Phone number cannot be empty. "
            "Please enter a valid number."
            f"{colors.END}"
        )
        return False


    try:
        parsed_number = phonenumbers.parse(phone_number)

    except NumberParseException:
        print(
            f"\n{colors.RED}"
            "[!] The phone number could not be parsed. "
            "Use the international format, such as +212612345678."
            f"{colors.END}"
        )
        return False


    if not phonenumbers.is_possible_number(parsed_number):
        print(
            f"\n{colors.RED}"
            "[!] The phone number is not possible."
            f"{colors.END}"
        )
        return False


    if not phonenumbers.is_valid_number(parsed_number):
        print(
            f"\n{colors.RED}"
            "[!] The phone number is not valid."
            f"{colors.END}"
        )
        return False
    
    print(
        f"\n{colors.GREEN}"
        "[+] The phone number is valid."
        f"{colors.END}"
    )
    return True
