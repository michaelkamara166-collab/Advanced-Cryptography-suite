"""
Hybrid Encryption Module
AES + RSA
"""

from crypto.aes import encrypt_file, decrypt_file, generate_key
from crypto.rsa import encrypt_key, decrypt_key


def hybrid_encrypt(file_path):

    aes_key = generate_key()

    encrypt_file(
        file_path,
        file_path + ".enc",
        aes_key
    )

    encrypted_key = encrypt_key(aes_key)

    with open(file_path + ".key", "wb") as f:
        f.write(encrypted_key)

    print("Hybrid encryption completed.")


def hybrid_decrypt(enc_file, key_file, output):

    with open(key_file, "rb") as f:
        encrypted_key = f.read()

    aes_key = decrypt_key(encrypted_key)

    decrypt_file(
        enc_file,
        output,
        aes_key
    )

    print("Hybrid decryption completed.")
