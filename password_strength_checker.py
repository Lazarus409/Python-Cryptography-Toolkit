#!/usr/bin/env python3
"""
Password strength validation and analysis
"""

import string


class PasswordStrengthChecker:
    """Validates and analyzes password strength"""
    
    @staticmethod
    def validate_password_strength(password: str) -> dict:
        """
        Validate password strength and return detailed feedback
        
        Args:
            password (str): The password to validate
            
        Returns:
            dict: {
                'is_strong': bool,
                'issues': list,
                'score': int (0-100),
                'feedback': str
            }
        """
        feedback = {
            'is_strong': True,
            'issues': [],
            'score': 100
        }
        
        # Check minimum length
        if len(password) < 8:
            feedback['issues'].append("Password must be at least 8 characters long")
            feedback['is_strong'] = False
            feedback['score'] -= 20
        
        # Check for uppercase
        if not any(c.isupper() for c in password):
            feedback['issues'].append("Password must contain at least one uppercase letter")
            feedback['is_strong'] = False
            feedback['score'] -= 15
        
        # Check for lowercase
        if not any(c.islower() for c in password):
            feedback['issues'].append("Password must contain at least one lowercase letter")
            feedback['is_strong'] = False
            feedback['score'] -= 15
        
        # Check for digits
        if not any(c.isdigit() for c in password):
            feedback['issues'].append("Password must contain at least one digit")
            feedback['is_strong'] = False
            feedback['score'] -= 15
        
        # Check for special characters
        if not any(c in string.punctuation for c in password):
            feedback['issues'].append("Password must contain at least one special character")
            feedback['is_strong'] = False
            feedback['score'] -= 15
        
        # Bonus for extra length
        if len(password) >= 12:
            feedback['score'] = min(100, feedback['score'] + 10)
        if len(password) >= 16:
            feedback['score'] = min(100, feedback['score'] + 10)
        
        # Generate feedback message
        if feedback['score'] >= 80:
            feedback['feedback'] = "Strong password"
        elif feedback['score'] >= 60:
            feedback['feedback'] = "Moderate password"
        elif feedback['score'] >= 40:
            feedback['feedback'] = "Weak password"
        else:
            feedback['feedback'] = "Very weak password"
        
        return feedback


if __name__ == '__main__':
    # Example usage
    checker = PasswordStrengthChecker()
    
    test_passwords = [
        "weak",
        "MyPassword123!",
        "test1234",
        "Correct-Horse-Battery-Staple123!"
    ]
    
    for password in test_passwords:
        result = checker.validate_password_strength(password)
        print(f"\nPassword: {'*' * len(password)}")
        print(f"Strength: {result['feedback']} (Score: {result['score']}/100)")
        print(f"Is Strong: {result['is_strong']}")
        if result['issues']:
            print("Issues:")
            for issue in result['issues']:
                print(f"  - {issue}")
