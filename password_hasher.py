#!/usr/bin/env python3
"""
Password hashing and verification utilities
"""

import hashlib
import secrets
from typing import Tuple


class PasswordHasher:
    """Handles password hashing and verification with salt"""
    
    def __init__(self, algorithm='sha256'):
        """
        Initialize the hasher with a specific algorithm
        
        Args:
            algorithm (str): 'sha256' or 'sha512'. Defaults to 'sha256'.
        """
        self.algorithm = algorithm
    
    def hash_password(self, password: str, salt: str = None) -> Tuple[str, str]:
        """
        Hash a password using the specified algorithm with a salt
        
        Args:
            password (str): The password to hash
            salt (str): Optional salt. If None, a random salt is generated
            
        Returns:
            tuple: (hashed_password, salt)
        """
        if salt is None:
            salt = secrets.token_hex(16)
        
        if self.algorithm == 'sha256':
            hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        elif self.algorithm == 'sha512':
            hashed = hashlib.sha512((password + salt).encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")
        
        return hashed, salt
    
    def verify_password(self, password: str, hashed_password: str, salt: str) -> bool:
        """
        Verify a password against a hashed password
        
        Args:
            password (str): The password to verify
            hashed_password (str): The stored hashed password
            salt (str): The salt used during hashing
            
        Returns:
            bool: True if password matches, False otherwise
        """
        computed_hash, _ = self.hash_password(password, salt)
        return computed_hash == hashed_password


if __name__ == '__main__':
    # Example usage
    hasher = PasswordHasher()
    
    # Hash a password
    password = "MySecurePassword123!"
    hashed, salt = hasher.hash_password(password)
    print(f"Password: {password}")
    print(f"Hashed: {hashed}")
    print(f"Salt: {salt}")
    
    # Verify password
    is_valid = hasher.verify_password(password, hashed, salt)
    print(f"Password verification: {is_valid}")
