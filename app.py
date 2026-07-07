from crypto.rsa import generate_keys
from crypto.hybrid import hybrid_encrypt, hybrid_decrypt
from crypto.hashing import sha256_hash, sha512_hash
from crypto.signature import sign_file, verify_signature

print("=" * 60)
print(" ADVANCED CRYPTOGRAPHY SUITE ")
print("=" * 60)

while True:

    print("""
1. Generate RSA Keys
2. Hybrid Encrypt File
3. Hybrid Decrypt File
4. SHA-256 Hash
5. SHA-512 Hash
6. Sign File
7. Verify Signature
8. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        generate_keys()

    elif choice == "2":
        filename = input("File: ")
        hybrid_encrypt(filename)

    elif choice == "3":
        enc = input("Encrypted File: ")
        key = input("Key File: ")
        output = input("Output File: ")

        hybrid_decrypt(enc, key, output)

    elif choice == "4":
        filename = input("File: ")
        print(sha256_hash(filename))

    elif choice == "5":
        filename = input("File: ")
        print(sha512_hash(filename))

    elif choice == "6":
        filename = input("File: ")
        sign_file(filename)

    elif choice == "7":
        filename = input("File: ")
        verify_signature(filename)

    elif choice == "8":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")
