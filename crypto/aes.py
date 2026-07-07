"""
AES-256 File Encryption Module
Advanced Cryptography Suite
Author: Michael Alfred Francis Kamara
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

BLOCK_SIZE = 16
KEY_SIZE = 32  # AES-256 = 32 bytes


def generate_key():
    """Generate a secure 256-bit AES key."""
    return get_random_bytes(KEY_SIZE)


def save_key(key, filename="keys/aes.key"):
    """Save AES key to a file."""
    os.makedirs("keys", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(key)


def load_key(filename="keys/aes.key"):
    """Load AES key from a file."""
    with open(filename, "rb") as f:
        return f.read()


def encrypt_file(input_file, output_file, key):
    """
    Encrypt a file using AES-256 CBC mode.
    """
    cipher = AES.new(key, AES.MODE_CBC)

    with open(input_file, "rb") as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))

    with open(output_file, "wb") as f:
        # Store IV first, then ciphertext
        f.write(cipher.iv)
        f.write(ciphertext)

    print(f"[+] File encrypted successfully: {output_file}")


def decrypt_file(input_file, output_file, key):
    """
    Decrypt a previously encrypted AES file.
    """
    with open(input_file, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)

    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"[+] File decrypted successfully: {output_file}")
