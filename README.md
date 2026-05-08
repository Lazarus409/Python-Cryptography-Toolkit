# Python-Cryptography-Toolkit

A comprehensive Python toolkit for cryptographic operations including password management and file encryption.

## Overview

This toolkit provides a collection of modules for secure password handling and file encryption operations:

- **Password Hashing** - Secure password hashing and verification with SHA-256/SHA-512
- **Password Generation** - Cryptographically secure random password generation
- **Password Strength Checking** - Comprehensive password strength validation with detailed feedback
- **File Encryption** - File encryption and decryption using Fernet (symmetric encryption)

## Installation

### Requirements

- Python 3.8+
- pip package manager

### Setup

1. Clone or download the project
2. Navigate to the project directory
3. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

4. Activate the virtual environment:
   - **Windows (PowerShell):**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   - **Windows (Command Prompt):**

   ```cmd
   .venv\Scripts\activate.bat
   ```

   - **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## File Structure

```
Python-Cryptography-Toolkit/
│
├── password_hasher.py              # Password hashing and verification
├── password_generator.py            # Secure password generation
├── file_encryptor.py               # File encryption/decryption
├── password_strength_checker.py    # Password strength validation
├── requirements.txt                # Project dependencies
└── README.md                       # This file
```

## Usage Examples

### Password Hasher

Hash and verify passwords securely with SHA-256 or SHA-512:

```python
from password_hasher import PasswordHasher

hasher = PasswordHasher(algorithm='sha256')

# Hash a password
hashed, salt = hasher.hash_password("MySecurePassword123!")
print(f"Hashed: {hashed}")
print(f"Salt: {salt}")

# Verify a password
is_valid = hasher.verify_password("MySecurePassword123!", hashed, salt)
print(f"Password valid: {is_valid}")
```

**Run standalone:**

```bash
python password_hasher.py
```

### Password Generator

Generate cryptographically secure random passwords:

```python
from password_generator import PasswordGenerator

generator = PasswordGenerator()

# Generate a 16-character password with all character types
secure_pwd = generator.generate_secure_password(length=16)
print(f"Generated password: {secure_pwd}")

# Custom character sets
pwd = generator.generate_secure_password(
    length=20,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True
)
print(f"Custom password: {pwd}")
```

**Run standalone:**

```bash
python password_generator.py
```

### Password Strength Checker

Validate password strength with detailed scoring and feedback:

```python
from password_strength_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker()

# Check password strength
result = checker.validate_password_strength("MyPassword123!")
print(f"Is strong: {result['is_strong']}")
print(f"Score: {result['score']}/100")
print(f"Feedback: {result['feedback']}")

if result['issues']:
    print("Issues:")
    for issue in result['issues']:
        print(f"  - {issue}")
```

**Run standalone:**

```bash
python password_strength_checker.py
```

### File Encryptor

Encrypt and decrypt files using Fernet (symmetric encryption):

```python
from file_encryptor import FileEncryptor

encryptor = FileEncryptor()

# Generate and save a key
key = encryptor.generate_key()
encryptor.save_key(key, 'my_key.key')

# Encrypt a file
encryptor.encrypt_file('sensitive_file.txt', 'sensitive_file.encrypted', key)
print("File encrypted successfully")

# Decrypt a file
loaded_key = encryptor.load_key('my_key.key')
encryptor.decrypt_file('sensitive_file.encrypted', 'sensitive_file_decrypted.txt', loaded_key)
print("File decrypted successfully")
```

**Run standalone:**

```bash
python file_encryptor.py
```

## Features

- **SHA-256/SHA-512 Hashing**: Multiple hashing algorithms with automatic salt generation
- **Cryptographic Randomness**: Uses `secrets` module for secure password generation
- **Customizable Passwords**: Configure character sets (uppercase, lowercase, digits, special)
- **Strength Scoring**: Password strength scoring (0-100) with detailed feedback and specific issues
- **Fernet Encryption**: Symmetric file encryption with authentication using the `cryptography` library
- **Key Management**: Simple utilities for key generation, storage, and loading

## Password Strength Requirements

A strong password score (80+) requires:

- ✓ At least 8 characters
- ✓ At least one uppercase letter
- ✓ At least one lowercase letter
- ✓ At least one digit
- ✓ At least one special character

Additional bonuses:

- +10 points for 12+ characters
- +10 points for 16+ characters

## Dependencies

The project uses the following packages (see `requirements.txt`):

- **cryptography** (v41.0.0+) - For file encryption with Fernet
- **Flask** (v3.0.0+) - Web framework (available for future web interface)
- **pynput** (v1.7.6+) - Input library (available for future keyboard monitoring)

Install with:

```bash
pip install -r requirements.txt
```

## Security Considerations

- **Salt Generation**: Each password is hashed with a unique 16-byte random salt
- **Algorithm**: SHA-256 by default (SHA-512 available for higher security)
- **Randomness**: All random operations use `secrets` module for cryptographic-grade security
- **File Encryption**: Fernet provides authenticated encryption
- **Key Management**:
  - Store encryption keys securely, separate from encrypted files
  - Never commit keys to version control
  - Never log or transmit keys in plain text
- **Password Storage**: Never store plain text passwords in production environments

## License

This project is provided as-is for educational and security purposes.

## Author

Lazarus Tiborweh

Created May 2026
