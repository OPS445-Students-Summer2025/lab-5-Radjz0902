#!/usr/bin/env python3
# Author ID: Radjznairene Jallorina

def read_file_string(file_name):
    """Return the entire contents of *file_name* as one string."""
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def read_file_list(file_name):
    """
    Return the contents of *file_name* as a list of lines
    with trailing newline characters removed.
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name), end='')  # end='' prevents extra blank line
    print()  # blank line to match sample output separation
    print(read_file_list(file_name))
