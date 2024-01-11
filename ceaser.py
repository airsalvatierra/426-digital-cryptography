SHIFT = 17

def caesar_cipher(text, shift, mode="encrypt"):
    """Encrypts or decrypts text using the Caesar cipher.

    Args:
        text (str): The text to encrypt or decrypt.
        shift (int): The number of positions to shift the letters.
        mode (str, optional): "encrypt" or "decrypt". Defaults to "encrypt".

    Returns:
        str: The encrypted or decrypted text.
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    if mode == "decrypt":
        shift = -shift
        table = str.maketrans(shifted_alphabet, alphabet)

    return text.translate(table)

message = input('Enter the message: ').strip()
action = input('Choose 1) Encrypt or 2) Decrypt: ')
while action not in ['1', '2']:
    action = input('Wrong choice, select of of the valid choices 1) Encrypt or 2) Decrypt: ')

print(
    caesar_cipher(message.lower(), SHIFT, 'decrypt' if action == '2' else 'encrypt')
)
