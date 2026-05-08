#!/usr/bin/env python3
"""
Secure password generation utilities
"""

import secrets
import string


class PasswordGenerator:
    """Generates cryptographically secure passwords"""
    
    @staticmethod
    def generate_secure_password(length: int = 16, 
                                use_uppercase: bool = True,
                                use_lowercase: bool = True,
                                use_digits: bool = True,
                                use_special: bool = True) -> str:
        """
        Generate a secure random password
        
        Args:
            length (int): Length of the password. Defaults to 16.
            use_uppercase (bool): Include uppercase letters. Defaults to True.
            use_lowercase (bool): Include lowercase letters. Defaults to True.
            use_digits (bool): Include digits. Defaults to True.
            use_special (bool): Include special characters. Defaults to True.
            
        Returns:
            str: A secure random password
        """
        characters = ''
        
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            raise ValueError("At least one character type must be enabled")
        
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password


if __name__ == '__main__':
    # Example usage
    generator = PasswordGenerator()
    
    print("Generated secure passwords:")
    for i in range(5):
        pwd = generator.generate_secure_password(length=16)
        print(f"  {i+1}. {pwd}")
