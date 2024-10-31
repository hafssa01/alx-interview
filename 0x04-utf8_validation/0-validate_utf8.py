#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Parameters:
    - data (list): List of integers representing bytes of data
    
    Returns:
    - bool: True if data is valid UTF-8, False otherwise
    """
    num_bytes = 0  # Number of expected continuation bytes

    for byte in data:
        # Mask to extract the least significant 8 bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Check how many leading 1 bits are in the first byte
            if (byte >> 5) == 0b110:   # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7) != 0:  # 1-byte character must start with 0
                return False
        else:
            # Check that byte is a continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
        num_bytes -= 1

    return num_bytes == 0
