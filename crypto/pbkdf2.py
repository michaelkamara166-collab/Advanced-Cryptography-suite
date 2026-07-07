"""
PBKDF2 Password-Based Key Derivation
"""

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

SALT_SIZE = 16
ITERATIONS = 100000
KEY_SIZE = 32


def derive_key(password, salt=None):
    if salt is None:
        salt = get_random_bytes(SALT_SIZE)

    key = PBKDF2(
        password,
        salt,
        dkLen=KEY_SIZE,
        count=ITERATIONS
    )

    return key, salt
