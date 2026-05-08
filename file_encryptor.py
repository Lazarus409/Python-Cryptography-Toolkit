#!/usr/bin/env python3
"""
File encryption and decryption utilities
"""

import os
from cryptography.fernet import Fernet


class FileEncryptor:
    """Handles file encryption and decryption using Fernet (symmetric encryption)"""
    
    @staticmethod
    def generate_key() -> bytes:
        """
        Generate a new encryption key
        
        Returns:
            bytes: A valid Fernet key
        """
        return Fernet.generate_key()
    
    @staticmethod
    def save_key(key: bytes, filename: str = 'encryption.key') -> None:
        """
        Save encryption key to a file
        
        Args:
            key (bytes): The encryption key
            filename (str): Path to save the key file
        """
        with open(filename, 'wb') as key_file:
            key_file.write(key)
    
    @staticmethod
    def load_key(filename: str = 'encryption.key') -> bytes:
        """
        Load encryption key from a file
        
        Args:
            filename (str): Path to the key file
            
        Returns:
            bytes: The loaded encryption key
        """
        with open(filename, 'rb') as key_file:
            return key_file.read()
    
    @staticmethod
    def encrypt_file(input_file: str, output_file: str, key: bytes) -> None:
        """
        Encrypt a file using the provided key
        
        Args:
            input_file (str): Path to the file to encrypt
            output_file (str): Path to save the encrypted file
            key (bytes): The encryption key
        """
        fernet = Fernet(key)
        
        with open(input_file, 'rb') as f:
            file_data = f.read()
        
        encrypted_data = fernet.encrypt(file_data)
        
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
    
    @staticmethod
    def decrypt_file(input_file: str, output_file: str, key: bytes) -> None:
        """
        Decrypt a file using the provided key
        
        Args:
            input_file (str): Path to the encrypted file
            output_file (str): Path to save the decrypted file
            key (bytes): The encryption key
        """
        fernet = Fernet(key)
        
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = fernet.decrypt(encrypted_data)
        
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)


if __name__ == '__main__':
    # Example usage
    encryptor = FileEncryptor()
    
    # Generate and save a key
    key = encryptor.generate_key()
    encryptor.save_key(key, 'test_key.key')
    print("Key generated and saved to 'test_key.key'")
    
    # Create a test file
    test_file = 'test_file.txt'
    with open(test_file, 'w') as f:
        f.write("This is a secret message!")
    print(f"Test file created: {test_file}")
    
    # Encrypt the file
    encrypted_file = 'test_file.encrypted'
    encryptor.encrypt_file(test_file, encrypted_file, key)
    print(f"File encrypted: {encrypted_file}")
    
    # Decrypt the file
    decrypted_file = 'test_file_decrypted.txt'
    encryptor.decrypt_file(encrypted_file, decrypted_file, key)
    print(f"File decrypted: {decrypted_file}")
    
    # Verify
    with open(decrypted_file, 'r') as f:
        print(f"Decrypted content: {f.read()}")
    
    # Cleanup
    os.remove(test_file)
    os.remove(encrypted_file)
    os.remove(decrypted_file)
    os.remove('test_key.key')
