#!/usr/bin/env python3
# Author ID: 144342235

def add(number1, number2):
    """
    Attempts to convert both inputs to integers and return their sum.
    If conversion fails, return a specific error string.
    """
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """
    Attempts to read all lines from the file specified by *filename*.
    Returns a list of lines or a specific error string on failure.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                   # 15
    print(add('10', 5))                # 15
    print(add('abc', 5))               # error
    print(read_file('seneca2.txt'))    # valid read
    print(read_file('file10000.txt'))  # error
