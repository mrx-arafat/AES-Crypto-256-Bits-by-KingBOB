# AES Encryption and Decryption

This repository contains Python scripts for encrypting and decrypting text files using the Advanced Encryption Standard (AES) in Cipher Block Chaining (CBC) mode with a 256-bit key. The scripts handle the encryption and decryption process and are designed to be user-friendly and secure.

## Overview

AES is a symmetric encryption algorithm widely used across the globe. This project implements AES-256, which means it uses a key size of 256 bits, providing a high level of security.

The CBC mode of operation enhances the security of the encryption process by XORing each block of plaintext with the previous ciphertext block before encrypting it. This project also implements Base64 encoding to ensure the encrypted data is ASCII text, which is easier to handle and transmit.

## Features

- **AES-256 Encryption**: Utilizes a 256-bit key for encryption, offering robust security.
- **CBC Mode**: Uses Cipher Block Chaining mode for more secure encryption.
- **IV (Initialization Vector)**: Employs a random IV for each encryption operation to ensure unique ciphertexts for the same plaintext.
- **Base64 Encoding**: Encodes the ciphertext and IV in Base64 for easy storage and transmission.

## Files in the Repository

- `encrypt.py`: Script to encrypt a text file (`plain.txt`) using AES-256 in CBC mode.
- `decrypt.py`: Script to decrypt the encrypted file (`encrypted.txt`) back to its original form.

## Usage

1. **Encryption**: Place your plaintext in `plain.txt` and run `full_aes_encrypt.py`. The script will generate an `encrypted.txt` file, which contains the Base64 encoded ciphertext.

2. **Decryption**: Run `full_aes_decrypt.py` to decrypt the content of `encrypted.txt`. The decrypted text will be saved in `output.txt`.

## Key and IV Handling

- The encryption key is a predefined 32-character string, ensuring compliance with AES-256 requirements.
- The IV is generated randomly for each encryption operation and is included with the ciphertext in `encrypted.txt`.

## Security Notes

- The key is hardcoded for demonstration purposes. In a production environment, ensure to manage the encryption key securely.
- Keep the `encrypted.txt` secure as it contains your encrypted data.

## Dependencies

- Python 3
- PyCryptodome library

## Installation

Ensure you have Python 3 and the PyCryptodome library installed. You can install PyCryptodome using pip:

```bash
pip install pycryptodome
