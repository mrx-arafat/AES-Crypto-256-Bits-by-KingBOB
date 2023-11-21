
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def aes_decrypt_cbc(cipher_text, key):
    iv = cipher_text[:AES.block_size]
    cipher_text = cipher_text[AES.block_size:]
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()

# User-provided key
key = 'KingBOB'  # This should be the same key used for encryption

# Check if 'encrypted.txt' exists
if not os.path.isfile('encrypted.txt'):
    print("encrypted.txt file not found.")
else:
    # Read the encrypted text from 'encrypted.txt'
    with open('encrypted.txt', 'rb') as encrypted_file:
        encrypted_text = encrypted_file.read()

    # Decrypt the text
    decrypted_text = aes_decrypt_cbc(encrypted_text, key)

    # Write the decrypted text to 'output.txt'
    with open('output.txt', 'w') as output_file:
        output_file.write(decrypted_text)
