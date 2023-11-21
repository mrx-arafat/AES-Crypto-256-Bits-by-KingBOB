
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

def aes_encrypt_cbc(plain_text, key, iv):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    return cipher.encrypt(pad(plain_text.encode(), AES.block_size))

# User-provided key and IV
key = 'Your32CharacterLongSecretKeyHere'  # Replace with your 32-character key
iv = get_random_bytes(AES.block_size)  # Random IV for CBC mode

# Check if plain.txt exists
if not os.path.isfile('plain.txt'):
    print("plain.txt file not found.")
else:
    # Read the plaintext from the file
    with open('plain.txt', 'r') as plain_file:
        plain_text = plain_file.read()

    # Encrypt the text
    encrypted_text = aes_encrypt_cbc(plain_text, key, iv)

    # Base64 encode the result (IV + encrypted text)
    encrypted_text_b64 = base64.b64encode(iv + encrypted_text)

    # Write the encrypted text to 'encrypted.txt'
    with open('encrypted.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_text_b64)
