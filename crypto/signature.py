from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def sign_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    with open("keys/private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    h = SHA256.new(data)

    signature = pkcs1_15.new(private_key).sign(h)

    with open(file_path + ".sig", "wb") as f:
        f.write(signature)

    print("[+] Signature Created")


def verify_signature(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    with open(file_path + ".sig", "rb") as f:
        signature = f.read()

    with open("keys/public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    h = SHA256.new(data)

    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("[+] Signature VALID")
    except (ValueError, TypeError):
        print("[-] Signature INVALID")
