#!/usr/bin/env python3
# Author ID: 144342235

# ----------  Reading helpers from lab5a.py  ----------
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

# ----------  NEW writing helpers for lab5b.py  ----------
def append_file_string(file_name, string_of_lines):
    """Append *string_of_lines* to the end of *file_name* (creates file if missing)."""
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """
    Overwrite *file_name* with each element from *list_of_lines*,
    placing each element on its own line.
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in list_of_lines:
            f.write(f'{line}\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Read every line from *file_name_read* and copy it into *file_name_write*,
    prefixing each copied line with an incremental line number and a colon.
    """
    with open(file_name_read, 'r', encoding='utf-8') as src, \
         open(file_name_write, 'w', encoding='utf-8') as dst:
        for idx, line in enumerate(src, start=1):
            dst.write(f'{idx}:{line.rstrip(chr(10))}\n')   # chr(10) == '\n'

# ----------  Demo / test block  ----------
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
