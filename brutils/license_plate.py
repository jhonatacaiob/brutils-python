import re
from typing import Optional
from random import choice, randint
from string import ascii_uppercase

# FORMATTING
############


def convert_to_mercosul(license_plate: str) -> Optional[str]:
    """
    Receives an old pattern license plate (LLLNNNN) and returns a Mercosul
    converted license plate (LLLNLNN). Input should be
    a digit string of proper length. In case of an invalid license plate
    it will return 'None'.
    Ex: ABC4567 - > ABC4F67
        ABC4*67 - > 'None'
    """
    if not is_valid_license_plate_old_format(license_plate):
        return None

    digits = [letter for letter in license_plate.upper()]
    digits[4] = chr(ord("A") + int(digits[4]))
    return "".join(digits)


def format(license_plate: str) -> Optional[str]:
    """
    Receives a license plate in any pattern (LLLNNNN or LLLNLNN) and returns a
    formatted version, with a dash (-) for the old pattern, in upper case for
    them Mercosul pattern and 'None' for an invalid license plate.
    Ex: ABC1234 - > ABC-1234
        abc1e34 - > ABC1E34
        ABC123  - > 'None'
    """
    license_plate = license_plate.upper()
    if is_valid_license_plate_old_format(license_plate):
        return license_plate[0:3] + "-" + license_plate[3:]
    elif is_valid_mercosul(license_plate):
        return license_plate.upper()
    return None


# OPERATIONS
############


def is_valid(license_plate: str) -> bool:
    """
    Checks wheter license plate is valid according to the old format and
    the Mercosul one.
    """
    return is_valid_license_plate_old_format(
        license_plate
    ) or is_valid_mercosul(license_plate)


def is_valid_license_plate_old_format(license_plate: str) -> bool:
    """
    Checks whether a string matches the old format of Brazilian license plate.
    """
    pattern = re.compile(r"^[A-Za-z]{3}[0-9]{4}$")
    return (
        isinstance(license_plate, str)
        and re.match(pattern, license_plate.strip()) is not None
    )


def is_valid_mercosul(license_plate: str) -> bool:
    """
    Returns whether or not the provided license_plate is valid according to the
    Mercosul pattern (LLLNLNN). Input should be a digit string of proper
    length. Ex: ABC4E67
    """
    if not isinstance(license_plate, str):
        return False

    license_plate = license_plate.upper().strip()
    pattern = re.compile(r"^[A-Z]{3}\d[A-Z]\d{2}$")
    return re.match(pattern, license_plate) is not None


def remove_symbols(license_plate_number: str) -> str:
    """Removes the dash (-) symbol from a license plate string.

    Args:
                    license_plate_number[str]: A license plate string
    Returns:
                    [str]: A license plate string without symbols
    """
    return license_plate_number.replace("-", "")


def get_format(license_plate: str) -> Optional[str]:
    """
    Returns the format of a license plate string without symbols. Returns
    'LLLNNNN' for the old pattern and 'LLLNLNN' for the Mercosul one.

    Args:
        license_plate[str]: A license plate string without symbols

    Returns:
        value[str]: The format of the license plate

        value[None]: For invalid license plates
    """

    if is_valid_license_plate_old_format(license_plate):
        return "LLLNNNN"

    if is_valid_mercosul(license_plate):
        return "LLLNLNN"

    return None


def generate(format="LLLNLNN"):  # type: (str) -> str | None
    """
    Generate a valid license plate in the given format. In case no format is
    provided, it will return a license plate in the Mercosul format.
    """
    generated = ""
    format = format.upper()
    if format not in ("LLLNLNN", "LLLNNNN"):
        return None
    for char in format:
        if char == "L":
            generated += choice(ascii_uppercase)
        else:
            generated += str(randint(0, 9))
    return generated
