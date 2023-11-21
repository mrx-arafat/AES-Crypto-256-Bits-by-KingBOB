
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os

def aes_decrypt_cbc(cipher_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()

# User-provided key
key = 'KingBOBKeyForAES256Encryption6X9'  
key = key.encode()  # Ensure the key is in bytes

# Check if 'encrypted.txt' exists
if not os.path.isfile('encrypted.txt'):
    print("encrypted.txt file not found.")
else:
    # Read the base64 encoded encrypted text from 'encrypted.txt'
    with open('encrypted.txt', 'rb') as encrypted_file:
        encrypted_text_b64 = encrypted_file.read()

    # Base64 decode the encrypted text
    encrypted_text = base64.b64decode(encrypted_text_b64)
    iv = encrypted_text[:AES.block_size]  # Extract the IV from the beginning
    encrypted_text = encrypted_text[AES.block_size:]

    # Decrypt the text
    decrypted_text = aes_decrypt_cbc(encrypted_text, key, iv)

    # Write the decrypted text to 'output.txt'
    with open('output.txt', 'w') as output_file:
        output_file.write(decrypted_text)
