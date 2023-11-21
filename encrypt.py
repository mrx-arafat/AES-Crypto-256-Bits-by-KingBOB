
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def aes_encrypt_cbc(plain_text, key):
    iv = os.urandom(AES.block_size)  # Using os.urandom for IV generation
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(plain_text.encode(), AES.block_size))

# My key
key = 'KingBOB'  # This should be 16, 24, or 32 bytes long for AES-128, AES-192, or AES-256

# Check if plain.txt exists
if not os.path.isfile('plain.txt'):
    print("plain.txt file not found.")
else:
    # Read the plaintext from the file
    with open('plain.txt', 'r') as plain_file:
        plain_text = plain_file.read()

    # Encrypt the text
    encrypted_text = aes_encrypt_cbc(plain_text, key)

    # Write the encrypted text to 'encrypted.txt'
    with open('encrypted.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_text)
