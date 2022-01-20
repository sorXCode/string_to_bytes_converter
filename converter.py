prefix_var = "0x"


def convert_to_hex(value):
    """
    Convert string to hex.
    """
    value = str(value)
    return value.encode("utf-8").hex()


def pad_hex(hex_value, padding):
    """
    Pad hex value with zeros.
    """
    return hex_value.ljust(padding, "0")


def convert_hex_to_str(hex_value):
    """
    Convert hex to string.
    """
    try:
        hex_value = hex_value.split(prefix_var)[-1]  # remove prefix
        str_value = bytes.fromhex(hex_value).decode("utf-8")
        str_value = str_value.rstrip("\x00")
        return str_value
    except ValueError as e:
        raise ValueError(f"Invalid Input")


def convert_str_to_hex_and_pad(value, padding, with_prefix=True):
    """
    Convert string to hex and pad it with zeros.
    """
    hex_value = convert_to_hex(value)
    result = pad_hex(hex_value, padding)
    if with_prefix:
        return prefix_var + result
    return result
