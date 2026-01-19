import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = string.ascii_lowercase

if use_upper:
    characters += string.ascii_uppercase
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if not characters:
    print("No character types selected!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\nGenerated Password:")
    print(password)
