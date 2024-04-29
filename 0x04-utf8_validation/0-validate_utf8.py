#!/usr/bin/python3

"""Function to validate UTF-8 encoding"""


def validUTF8(data):
    """Validate UTF-8 encoding"""
    no_bytes = 0
    for num in data:
        mask = 1 << 7
        if no_bytes == 0:
            while mask & num:
                no_bytes += 1
                mask >>= 1
            if no_bytes == 0:
                continue
            if no_bytes == 1 or no_bytes > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False
        no_bytes -= 1
    return no_bytes == 0
