import pandas as pd


def validate_phone(phone_number):
    """ Ensure that phone numbers are in a valid format

    Keyword arguments:
    phone_number -- A Pandas Series of phone_numbers as strings.

    Returns: A boolean Pandas Series. Valid phone numbers are True, Invalid are False
    """
    bool_phone = phone_number.str.contains(r'^\d{3}[-]?\d{2}[-]?\d{3}')
    return bool_phone
numbers = pd.Series(['303-317-7129', '303-913-0349', '423-23-323'])
