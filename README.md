# Advanced Cryptography Suite

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red.svg)

## Overview

Advanced Cryptography Suite is a modular Python application that demonstrates modern cryptographic techniques used in cybersecurity. The project provides secure file encryption, digital signatures, hashing, password-based key derivation, and hybrid encryption using industry-standard algorithms.

This project was developed as part of a Cyber Security Internship to demonstrate practical knowledge of cryptography and secure software development.

---

# Features

- AES-256 File Encryption
- AES-256 File Decryption
- RSA-2048 Key Pair Generation
- Hybrid Encryption (AES + RSA)
- SHA-256 Hashing
- SHA-512 Hashing
- Digital Signature Generation
- Digital Signature Verification
- PBKDF2 Password-Based Key Derivation
- Secure Logging
- Menu-Driven Command-Line Interface
- Modular Python Architecture

---

# Technologies Used

- Python 3.10+
- PyCryptodome
- Cryptography
- Rich
- Colorama
- Hashlib

---

# Project Structure

```text
Advanced-Cryptography-Suite/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── crypto/
│   ├── __init__.py
│   ├── aes.py
│   ├── rsa.py
│   ├── hybrid.py
│   ├── hashing.py
│   ├── signature.py
│   ├── pbkdf2.py
│   └──  logger.py
│
├── keys/
├── encrypted/
├── decrypted/
├── samples/
└──screenshots/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/USERNAME/Advanced-Cryptography-Suite.git
```

Move into the project

```bash
cd Advanced-Cryptography-Suite
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate it

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python3 app.py
```

---

# Menu

```
==============================
Advanced Cryptography Suite
==============================

1. Generate RSA Keys
2. Hybrid Encrypt File
3. Hybrid Decrypt File
4. SHA-256 Hash
5. SHA-512 Hash
6. Sign File
7. Verify Signature
8. Exit
```

---

# Cryptographic Algorithms

## AES-256

- Symmetric Encryption
- 256-bit Key
- CBC Mode
- PKCS7 Padding
- Random Initialization Vector (IV)

---

## RSA-2048

- Public Key Encryption
- Private Key Decryption
- OAEP Padding
- Secure Key Exchange

---

## SHA-256

Produces a fixed-length 256-bit cryptographic hash for integrity verification.

---

## SHA-512

Produces a fixed-length 512-bit cryptographic hash for stronger integrity verification.

---

## Digital Signature

Uses RSA and SHA-256 to:

- Verify authenticity
- Verify integrity
- Prevent tampering

---

## Hybrid Encryption

1. Generate random AES key
2. Encrypt file using AES
3. Encrypt AES key using RSA
4. Store encrypted key
5. Decrypt AES key with RSA
6. Recover original file

---

# Example Workflow

Generate RSA Keys

↓

Encrypt File

↓

AES Key Generated

↓

AES Key Encrypted with RSA

↓

Encrypted File Saved

↓

Decrypt File

↓

Verify Digital Signature

---

# Security Features

- AES-256 Encryption
- RSA-2048 Encryption
- Secure Random Number Generation
- PBKDF2 Key Derivation
- Digital Signatures
- SHA-256 Integrity Checking
- SHA-512 Integrity Checking

---

# Learning Outcomes

This project demonstrates practical understanding of:

- Applied Cryptography
- Symmetric Encryption
- Asymmetric Encryption
- Hybrid Encryption
- Secure File Storage
- Digital Signatures
- Password Security
- Cryptographic Hash Functions
- Secure Python Development

---

# Future Improvements

- Graphical User Interface
- Drag-and-Drop File Encryption
- AES-GCM Support
- ECC Cryptography
- Multi-user Key Management
- Secure Cloud Backup
- Database Encryption
- Automated Unit Testing

---

# Author

Michael Alfred Francis Kamara

Cyber Security Student

---

# Acknowledgements

Special thanks to:

- Codec Technologies
- Python Software Foundation
- PyCryptodome Developers
- Open Source Community

---

# Disclaimer

This software is intended solely for educational purposes and authorized security testing. Users are responsible for ensuring they comply with all applicable laws and obtain proper authorization before using any security-related functionality.

---

# License

This project is licensed under the MIT License.
