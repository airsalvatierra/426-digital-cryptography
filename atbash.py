# Python program to implement Atbash Cipher
 
# This script uses dictionaries to lookup various alphabets
lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
 
def atbash(message, action='decrypt'):
    if action == 'decrypt':
        lookup = {value: key for key, value in lookup_table.items()}
    else:
        lookup = lookup_table.copy()

    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            #adds the corresponding letter from the lookup_table
            cipher += lookup[letter]
        else:
            # adds space
            cipher += ' '
 
    return cipher
 
# Driver function to run the program
message = input('Enter the message: ').strip()
action = input('Choose 1) Encrypt or 2) Decrypt: ')
while action not in ['1', '2']:
    action = input('Wrong choice, select of of the valid choices 1) Encrypt or 2) Decrypt: ')

print(atbash(message=message.upper(), action='decrypt' if action == '2' else 'encrypt'))
