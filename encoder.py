#!/usr/bin/env python3
"""Multi-mode Encoder/Decoder Tool."""
import base64
import codecs
import urllib.parse
import sys
import argparse

def base64_encode(text: str) -> str:
    """Encode text to Base64."""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def base64_decode(text: str) -> str:
    """Decode Base64 text. Raises an error if input is not valid Base64."""
    try:
        decoded_bytes = base64.b64decode(text.encode('utf-8'), validate=True)
        return decoded_bytes.decode('utf-8')
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        raise ValueError("Invalid Base64 input") from e
    
def hex_encode(text: str) -> str:
    """Encode text to Hex."""
    return text.encode('utf-8').hex()

def hex_decode(text: str) -> str:
    """Decode Hex text. Raises an error if input is not valid Hex."""
    try:
        decoded_bytes = bytes.fromhex(text)
        return decoded_bytes.decode('utf-8')
    except (ValueError, UnicodeDecodeError) as e:
        raise ValueError("Invalid Hex input") from e
    
def rot13(text: str) -> str:
    """Apply ROT13 encoding/decoding."""
    return codecs.encode(text, 'rot_13')

def caesar_cipher(text: str, shift: int=3, decode: bool=False) -> str:
    """Apply Caesar cipher encoding/decoding."""
    if decode:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def url_encode(text: str) -> str:
    """Encode text to URL encoding."""
    return urllib.parse.quote(text)

def url_decode(text: str) -> str:
    """Decode URL encoded text."""
    return urllib.parse.unquote(text)

def xor_cipher(text: str, key: int=42) -> str:
    """Apply XOR cipher encoding/decoding."""
    return ''.join(chr(ord(c) ^ key) for c in text)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Multi-mode Encoder/Decoder Tool")
    parser.add_argument("--mode", choices=["base64", "hex", "rot13", "caesar", "url",
                        "xor"], required=True, help="Encoding/decoding method")
    parser.add_argument("--encode", dest="encode", help="Encode the input")
    parser.add_argument("--decode", dest="decode", help="Decode the input")
    parser.add_argument("--shift", type=int, default=3, help="Shift value for Caesar cipher (default: 3)")
    parser.add_argument("--key", type=int, default=42, help="Key for XOR cipher (default: 42)")
    return parser

def menu():
    print("=== Encoder/Decoder Menu ===")
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. Hex Encode")
    print("4. Hex Decode")
    print("5. ROT13")
    print("6. Caesar Cipher Encode")
    print("7. Caesar Cipher Decode")
    print("8. URL Encode")
    print("9. URL Decode")
    print("10. XOR Cipher")
    print("0. Exit")

def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.mode == "base64":
            if args.encode:
                print(base64_encode(args.encode))
            elif args.decode:
                print(base64_decode(args.encode))
        elif args.mode == "hex":
            if args.encode:
                print(hex_encode(args.encode))
            elif args.decode:
                print(hex_decode(args.encode))
        elif args.mode == "rot13":
            if args.encode:
                print(rot13(args.encode))
            elif args.decode:
                print(rot13(args.encode))
        elif args.mode == "caesar":
            if args.encode:
                print(caesar_cipher(args.encode, args.shift))
            elif args.decode:
                print(caesar_cipher(args.encode, args.shift, decode=True))
        elif args.mode == "url":
            if args.encode:
                print(url_encode(args.encode))
            elif args.decode:
                print(url_decode(args.encode))
        elif args.mode == "xor":
            if args.encode:
                print(xor_cipher(args.encode, args.key))
            elif args.decode:
                print(xor_cipher(args.encode, args.key))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()