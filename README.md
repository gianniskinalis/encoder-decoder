# Multi-Mode Encoder/Decoder

A simple, educational **Python command-line tool** to encode and decode text using multiple methods. This project demonstrates **basic cryptography, encoding schemes, and CLI programming**.

---

## Features

- **Base64** encoding and decoding
- **Hexadecimal** encoding and decoding
- **ROT13** (symmetric encoding)
- **Caesar Cipher** with customizable shift
- **URL Encoding/Decoding**
- **XOR Cipher** with customizale key
- **CLI support** via `argparse` for interacive or scripted use

---

## Installation

### Linux / macOS

1. Clone or download this repository.
2. Make the script executable:
   ```bash
   chmod +x encoder.py
3. Move it to a folder in your PATH:
   ```bash
   sudo mv encoder.py /usr/local/bin/encoder
4. Test from anywhere:
   ```bash
   encoder --mode base64 --encode "hello world"

### Windows

1. Save `encoder.py` in a permanent folder e.g., `C:\tools`.
2. Create `encoder.bat` in the same folder.
   ```bash
   @echo off
   python C:\tools\encoder.py %*
3. Add `C:\tools` to your system PATH.
4. Test:
   ```bash
   encoder --mode base64 --encode "hello world"

---

## Example Usage

```bash
# Base64 encode
encoder --mode base64 --encode "hello world"
# Output: aGVsbG8gd29ybGQ

# Base64 decode
encoder --mode base64 --decode "aGVsbG8gd29ybGQ="
# Output: hello world

# Caesar cipher encode with shift 5
encoder --mode caesar --encode "attack at dawn" --shift 5
# Output: fyyfhp fy ifbs

# Caesar cipher decode with shift 5
encoder --mode caesar --decode "fyyfhp fy ifbs" --shift 5
# Output: attack at dawn
```

## Help Menu
```bash
encoder -h
```

## Development

- Written in Python 3.
- Uses `argparse` for CLI.
- Modular functions for each encoding/decoding method.
- Easily extendable:
  ```bash
  def new_cipher(text: str):
    pass

## License

This project is MIT Licensed. Feel free to use, modify, or extend it.
