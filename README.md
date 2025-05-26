# Caesar Cipher Tool

## Description
This is a simple Python-based Caesar Cipher tool that allows users to encrypt or decrypt messages using a classical shift-based encryption algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

This script provides a basic demonstration of encryption concepts and is suitable for beginners learning about ciphers, string manipulation, and control flow in Python.

## Features
- Supports both encryption and decryption
- Preserves case sensitivity (uppercase and lowercase)
- Ignores and retains non-alphabet characters (like punctuation and spaces)
- Simple and interactive command-line interface

## Usage
Run the script and follow the on-screen prompts to encrypt or decrypt a message:

```bash
python3 Caesar_Cipher.py
```

### Example
```
===== Caesar_Cipher_Tool =====
 Type 'encrypt' to encrypt or 'decrypt' to decrypt : encrypt
Enter your message : Hello World!
Enter shift value (e.g., 4) : 3

Result (Encrypted Text) : Khoor Zruog!
```

## Concepts Demonstrated
- ASCII manipulation with `ord()` and `chr()`
- Modulo arithmetic for wrap-around logic
- String traversal and conditional character processing
- Basic input/output interaction in Python

## Requirements
- Python 3.x
(No external libraries required)

## Disclaimer
This implementation is for educational purposes and not suitable for secure communications. The Caesar Cipher is a weak encryption method and can be easily broken with brute force.
