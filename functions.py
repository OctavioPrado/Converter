list_of_numbers = []

def logo():
    print('''
  ____                          _
 / ___|___  _ ____   _____ _ __| |_ ___ _ __
| |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |__| (_) | | | \ V /  __/ |  | ||  __/ |
 \____\___/|_| |_|\_/ \___|_|   \__\___|_|

by: S1ThN1x
''')

def menu():
    print('''
Options:

[0]-quit

[1]-decimal to binary [4]-binary to octal   [7]-octal to binary  [10]-hex to binary
[2]-decimal to octal  [5]-binary to decimal [8]-octal to decimal [11]-hex to octal
[3]-decimal to hex    [6]-binary to hex     [9]-octal to hex     [12]-hex to decimal

            ''')

#      Decimal functions
# ---------------------------

def decimal_binary():
    entry = input('Decimal Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        binary_numbers = bin(int(numbers))[2:]
        print(f'{numbers} --> {binary_numbers}')

def decimal_octal():
    entry = input('Decimal Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        octal_numbers = oct(int(numbers))[2:]
        print(f'{numbers} --> {octal_numbers}')

def decimal_hex():
    entry = input('Decimal Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        hex_numbers = hex(int(numbers))[2:]
        print(f'{numbers} --> {hex_numbers}')

#      Binary functions
# ---------------------------

def binary_octal():
    entry = input('Binary Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        octal_numbers = oct(int(numbers,2))[2:]
        print(f'{numbers} --> {octal_numbers}')

def binary_decimal():
    entry = input('Binary Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        decimal_numbers = int(numbers,2)
        print(f'{numbers} --> {decimal_numbers}')

def binary_hex():
    entry = input('Binary Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        hex_numbers = hex(int(numbers,2))[2:]
        print(f'{numbers} --> {hex_numbers}')

#      Octal functions
# ---------------------------

def octal_binary():
    entry = input('Octal Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        binary_numbers = bin(int(numbers,8))[2:]
        print(f'{numbers} --> {binary_numbers}')

def octal_decimal():
    entry = input('Octal Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        decimal_numbers = int(numbers,8)
        print(f'{numbers} --> {decimal_numbers}')

def octal_hex():
    entry = input('Octal Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        hex_numbers = hex(int(numbers,8))[2:]
        print(f'{numbers} --> {hex_numbers}')

#      Hex functions
# ---------------------------

def hex_binary():
    entry = input('Hex Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        binary_numbers = bin(int(numbers,16))[2:]
        print(f'{numbers} --> {binary_numbers}')

def hex_octal():
    entry = input('Hex Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        hex_numbers = oct(int(numbers,16))[2:]
        print(f'{numbers} --> {hex_numbers}')

def hex_decimal():
    entry = input('Hex Numbers: ')
    list_of_numbers = entry.split()
    for numbers in list_of_numbers:
        decimal_numbers = int(numbers,16)
        print(f'{numbers} --> {decimal_numbers}')
