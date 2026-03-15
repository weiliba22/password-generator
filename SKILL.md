---
name: password-generator
description: Generate secure random passwords with customizable length and character sets
requiredEnv: []
permissions: []
source:
  url: https://github.com/weiliba22/password-generator
  author: jiec334
  verified: false
security:
  note: Pure Python script, no external dependencies, no network calls
---

# Password Generator

Generate secure, random passwords with customizable options.

## When to Use This

Use this skill when the user asks for:
- "Generate a password"
- "Create a secure password"
- "Make a random password"
- "I need a strong password"
- Password for any account or service

## Password Generation Options

| Option | Default | Description |
|--------|---------|-------------|
| Length | 16 | Number of characters |
| Uppercase | true | Include A-Z |
| Lowercase | true | Include a-z |
| Numbers | true | Include 0-9 |
| Symbols | true | Include !@#$%^&*() |

## Usage

### Basic Usage

Generate a default 16-character password:
```
python password_generator.py
```

### Custom Length

Generate a 24-character password:
```
python password_generator.py --length 24
```

### Only Letters

Generate password with only letters:
```
python password_generator.py --no-numbers --no-symbols
```

### Only Numbers (PIN)

Generate a 6-digit PIN:
```
python password_generator.py --length 6 --onlydigits
```

## Examples

| Command | Output Example |
|---------|----------------|
| `python password_generator.py` | `K9#mP2$vL5@nQ8xR` |
| `python password_generator.py --length 24` | `aB3$cD5%eF7&gH9#jK1...` |
| `python password_generator.py --length 6 --onlydigits` | `482931` |

## Constraints

- Maximum length: 128 characters
- Minimum length: 4 characters
- At least one character type must be enabled
- Uses Python's `secrets` module for cryptographically secure random generation
