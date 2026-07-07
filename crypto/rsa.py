"""
RSA-2048 Cryptography Module
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

KEY_SIZE = 2048


def generate_keys():
    os.makedirs("keys", exist_ok=True)

    key = RSA.generate(KEY_SIZE)

    with open("keys/private.pem", "wb") as f:
        f.write(key.export_key())

    with open("keys/public.pem", "wb") as f:
        f.write(key.publickey().export_key())

    print("[+] RSA Key Pair Generated")


def encrypt_key(aes_key):
    with open("keys/public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(aes_key)


def decrypt_key(encrypted_key):
    with open("keys/private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_key)
