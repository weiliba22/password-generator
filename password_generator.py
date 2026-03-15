#!/usr/bin/env python3
"""
Password Generator - Generate secure random passwords
"""

import argparse
import secrets
import string
import sys


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    only_digits: bool = False
) -> str:
    """Generate a secure random password."""
    
    if only_digits:
        return ''.join(secrets.choice(string.digits) for _ in range(length))
    
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        print("Error: At least one character type must be enabled", file=sys.stderr)
        sys.exit(1)
    
    # Ensure at least one character from each enabled type
    password = []
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))
    
    # Fill the rest randomly
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(secrets.choice(chars) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable positions
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(
        description='Generate secure random passwords'
    )
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=16,
        help='Password length (default: 16, max: 128)'
    )
    parser.add_argument(
        '--no-uppercase',
        action='store_true',
        help='Exclude uppercase letters'
    )
    parser.add_argument(
        '--no-lowercase',
        action='store_true',
        help='Exclude lowercase letters'
    )
    parser.add_argument(
        '--no-numbers',
        action='store_true',
        help='Exclude numbers'
    )
    parser.add_argument(
        '--no-symbols',
        action='store_true',
        help='Exclude special symbols'
    )
    parser.add_argument(
        '--onlydigits',
        action='store_true',
        help='Generate PIN (digits only)'
    )
    
    args = parser.parse_args()
    
    # Validate length
    if args.length < 4:
        print("Error: Minimum length is 4", file=sys.stderr)
        sys.exit(1)
    if args.length > 128:
        print("Error: Maximum length is 128", file=sys.stderr)
        sys.exit(1)
    
    password = generate_password(
        length=args.length,
        use_uppercase=not args.no_uppercase,
        use_lowercase=not args.no_lowercase,
        use_digits=not args.no_numbers,
        use_symbols=not args.no_symbols,
        only_digits=args.onlydigits
    )
    
    print(password)


if __name__ == '__main__':
    main()
