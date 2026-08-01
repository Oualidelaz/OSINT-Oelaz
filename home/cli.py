from appC.display import number_display
from app.scan_username import sc_username
from appB.get_ip import show_your_public_ip
from appB.ip_tracker import extract_ip_info
from appB.validation import ip_validation
from appC.validation import number_validation
from home.global_config import clean, home, Colors
from app.validation import username_validation
from appC.phone_tracker import extract_number_info
import sys


def main():
    try:
        colors = Colors()
        clean()
        home()
        print(f"{colors.GREEN}[1]{colors.END} Username Tracker")
        print(f"{colors.GREEN}[2]{colors.END} Phone Name Tracker")
        print(f"{colors.GREEN}[3]{colors.END} IP Tracker")
        print(f"{colors.GREEN}[4]{colors.END} Show Your IP")
        print(f"{colors.GREEN}[5]{colors.END} Exit\n")

        while True:
            choice = input(f"{colors.YELLOW}[+] Select an option: {colors.END}")
            try:
                choice = int(choice)
            except ValueError:
                print(f"\n{colors.RED}[!] Invalid choice. Please enter a number.{colors.END}")
                continue
            
            if choice:
                if choice in (1, 2, 3, 4, 5):
                    break
                else:
                    print(f"\n{colors.RED}[!] Invalid choice. Please select a number between 1 and 5.{colors.END}")
        
        if choice == 1:
            while True:
                username = (input(f"{colors.YELLOW}[+] Enter The username: {colors.END}")).strip()
                if username_validation(username):
                    break

            sc_username(username)


        if choice == 2:
            while True:
                phone_number = input(
                    f"{colors.YELLOW}"
                    "[+] Enter the phone number in international format "
                    "(e.g. +212612345678): "
                    f"{colors.END}"
                ).strip()

                if number_validation(phone_number):
                    break
        
            fields = extract_number_info(phone_number)
            if fields is None:
                print(
                    f"{colors.RED}"
                    "[!] Phone number information extraction failed."
                    f"{colors.END}"
                )
                sys.exit(1)
            
            number_display(fields)

        if choice == 3:
            while True:
                ip_addr = (input(f"{colors.YELLOW}[+] Enter The IP address: {colors.END}")).strip()
                if ip_validation(ip_addr):
                    break
            
            extract_ip_info(ip_addr)


        if choice == 4:
            show_your_public_ip()

        
        if choice == 5:
            print(
                f"\n{colors.LIGHT_RED}"
                "[+] Exiting the program safely."
                f"{colors.END}"
            )
            sys.exit(1)


                  
    except Exception as e:
        print(f"Error: {e}")

    except KeyboardInterrupt:
        print(f"\n\n{colors.RED}[!] Process interrupted. Exiting safely.{colors.END}")
        sys.exit(1)
