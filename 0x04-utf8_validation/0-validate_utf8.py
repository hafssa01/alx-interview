#!/usr/bin/python3

"""
method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8
    encoding.
    Args:
        data (List[int]): A lsit of integers representing bytes of data
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """

    # Number of bytes for the current character
    num_bytes = 0

    for byte in data:
        # If the most significant bit is 0, it's a one-byte character
        if num_bytes == 0:
            if (byte >> 7) == 0:
                num_bytes = 0
            # If the most significant bit is 10, it's not a valid
            # start byte
            elif (byte >> 6) == 0b10:
                return False
            # For multi-byte charactersm determine number of bytes
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # For multi-byte characters, the following bytes must
            # start with 10
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are remaining bytes expected for a character, it's invalid
    return num_bytes == 0