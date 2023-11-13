import re

from django.core.exceptions import ValidationError


def validate_only_letters_and_spaces(value):
    for letter in value:
        if not (letter.isalpha() or letter.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def validate_phone_number(value):
    COUNTRY_CODE = '+359'

    code = value[:3]
    if not (code == COUNTRY_CODE and (len(value) == 13 and value[4:].isdigit())):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")

    # regex solution
    # if not re.match(r'^\+359\d{9}$', value):
    #     raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
