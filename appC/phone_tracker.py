import pycountry
import phonenumbers
from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    carrier,
    geocoder,
    timezone,
)

def extract_number_info(phone_number: str) -> list[tuple[str, object]] | None:
    try:
        parsed_number = phonenumbers.parse(phone_number, None)


        # Formatted numbers
        e164_format = phonenumbers.format_number(
            parsed_number,
            PhoneNumberFormat.E164,
        )


        international_format = phonenumbers.format_number(
            parsed_number,
            PhoneNumberFormat.INTERNATIONAL,
        )


        national_format = phonenumbers.format_number(
            parsed_number,
            PhoneNumberFormat.NATIONAL,
        )

        rfc3966_format = phonenumbers.format_number(
            parsed_number,
            PhoneNumberFormat.RFC3966,
        )

        # Basic Information
        region_code = (
            phonenumbers.region_code_for_number(parsed_number)
            or "N/A"
        )

        # We use pycountry here to convert the country code returned by the phonenumbers library into the full country name.
        country = (
            pycountry.countries.get(alpha_2=region_code) # alpha_2 -> MA and alpha_3 -> MAR
            if region_code != "N/A"
            else None
        )

        country_name = (
            country.name
            if country is not None
            else "N/A"
        )

        # country_name = (
        #     geocoder.country_name_for_number(
        #         parsed_number,
        #         "en",
        #     )
        #     or "N/A"
        # )

        number_type_value = phonenumbers.number_type(
            parsed_number
        )

        number_type = PhoneNumberType.to_string(
            number_type_value
        )


        extension = parsed_number.extension or "N/A"


        # Metadata information
        time_zones = timezone.time_zones_for_number(
            parsed_number
        )

        time_zones_text = (
            ", ".join(time_zones)
            if time_zones
            else "N/A"
        )


        location = (
            geocoder.description_for_number(
                parsed_number,
                "en",
            )
            or "N/A"
        )


        service_provider = (
            carrier.name_for_number(
                parsed_number,
                "en",
            )
            or "N/A"
        )


        # Store results
        fields: list[tuple[str, object]] = [
            ("Phone Number", e164_format),
            ("International Format", international_format),
            ("National Format", national_format),
            ("RFC3966 Format", rfc3966_format),
            (
                "Country Calling Code",
                parsed_number.country_code,
            ),
            (
                "National Number",
                parsed_number.national_number,
            ),
            ("Region Code", region_code),
            ("Country", country_name),
            ("Number Type", number_type),
            ("Extension", extension),
            ("Timezone", time_zones_text),
            ("Location", location),
            ("Service Provider", service_provider),
        ]


        return fields

    except NumberParseException as error:
        print(
            "\n[!] Unable to parse the phone number."
        )
        print(f"    Error: {error}")
        return None
