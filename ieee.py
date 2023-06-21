import struct


def float_to_ieee(float_num):
    binary = struct.pack('>f', float_num)
    hex_code = ''.join(format(byte, '02X') for byte in binary)

    binary_code = ''.join(format(byte, '08b') for byte in binary)

    return hex_code, binary_code


def hex_to_binary(hex_code):
    binary_code = bin(int(hex_code, 16))[2:].zfill(len(hex_code) * 4)
    return binary_code


def binary_to_hex(binary_code):
    hex_code = hex(int(binary_code, 2))[2:].upper()
    return hex_code


def internal_to_ieee(hex_code):
    if len(hex_code) == 8:
        binary_code = hex_to_binary(hex_code)
    else:
        binary_code = hex_code
    if binary_code == '00000000000000000000000000000000':
        return binary_code, binary_to_hex(binary_code)
    sign = binary_code[0]
    exponent = binary_code[1:9]
    mantissa = binary_code[9:]

    sign_reverse = format(not int(sign, 2), '01b')
    exponent_ieee = format(int(int(exponent, 2) /2 + 127), '08b')
    ieee_code_binary = sign_reverse + exponent_ieee + mantissa
    ieee_code_hex = binary_to_hex(ieee_code_binary)
    return ieee_code_binary, ieee_code_hex


def ieee_to_internal(hex_code):
    if len(hex_code) == 8:
        binary_code = hex_to_binary(hex_code)
    else:
        binary_code = hex_code
    if binary_code == '00000000000000000000000000000000':
        return binary_code, binary_to_hex(binary_code)
    sign = binary_code[0]
    exponent = binary_code[1:9]
    mantissa = binary_code[9:]

    sign_reverse = format(not int(sign, 2), '01b')
    exponent_internal = format((int(exponent, 2) - 127)*2, '08b')
    internal_code_binary = sign_reverse + exponent_internal + mantissa
    internal_code_hex = binary_to_hex(internal_code_binary)
    return internal_code_binary, internal_code_hex


# Przykład użycia
internal = '8F7FFF00'
ieee = '477FFF00'

ie1, ie2 = internal_to_ieee(internal)
in1, in2 = ieee_to_internal(ieee)

print('Internal (', internal, ') > IEEE 754: ', ie1, '(', ie2, ')')
print('IEEE 754 (', ieee, ') > Internal: ', in1, '(', in2, ')')
