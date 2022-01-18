prefix_var = '0x'

def convert_to_hex(value):
    value = str(value)
    return value.encode('utf-8').hex()

def pad_hex(hex_value, padding):
    return hex_value.ljust(padding, '0')



def convert_and_pad(value, padding, with_prefix=True):
    hex_value = convert_to_hex(value)
    result = pad_hex(hex_value, padding)
    if with_prefix:
        return prefix_var+result
    return result