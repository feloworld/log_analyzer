# Password Generator

A small interactive Python utility for generating passwords and checking basic password composition requirements.

## Requirements

- Python 3
- No third-party packages

## Run

```powershell
python password_generator.py
```

**Security note:** this example uses Python's `random` module, which is not designed for cryptographic secrets. Do not use generated values for real accounts without replacing it with a cryptographically secure source such as `secrets`.