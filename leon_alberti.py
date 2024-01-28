import string

alphabet = string.ascii_lowercase
cipher_alphabets = ['fzbvkixaymeplsdhjorgnqcutw', 'goxbfwthqilapzjdesvycrkuhn']

def encrypt(plaintext):
    ciphertext = ""
    index = 0
    for char in plaintext:
        if char.isalpha():
            offset = index % 2
            ciphertext += cipher_alphabets[offset][alphabet.index(char.lower())]
            index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext):
    plaintext = ""
    index = 0
    for char in ciphertext:
        if char.isalpha():
            offset = index % 2
            plaintext += alphabet[cipher_alphabets[offset].index(char.lower())]
            index += 1
        else:
            plaintext += char
    return plaintext

message = input('Enter the message: ').strip().lower()
action = input('Choose 1) Encrypt or 2) Decrypt: ')
while action not in ['1', '2']:
    action = input('Wrong choice, select of of the valid choices 1) Encrypt or 2) Decrypt: ')

if action == '1':
    print(encrypt(message))
else:
    print(decrypt(message))
