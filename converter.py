import functions,os

options = {
    'on_off': True,
    1: functions.decimal_binary,
    2: functions.decimal_octal,
    3: functions.decimal_hex,
    4: functions.binary_octal,
    5: functions.binary_decimal,
    6: functions.binary_hex,
    7: functions.octal_binary,
    8: functions.octal_decimal,
    9: functions.octal_hex,
    10: functions.hex_binary,
    11: functions.hex_octal,
    12: functions.hex_decimal,
    }

functions.logo()

while options['on_off']:
    try:
        functions.menu()
        user = int(input('Select one option: '))

        if user == 0:
            print('\nGoodbye!\n')
            options['on_off'] = False
        else:
            os.system('clear')
            options.get(user)()

    except ValueError:
        print('\nSomenting wrong!')
    except TypeError:
        print('Invalid option!')
