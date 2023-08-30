import random
import string

def generate_password(min_length, include_numbers=True, include_special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if include_numbers:
        characters += digits
    if include_special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if include_numbers:
            meets_criteria = meets_criteria and has_number
        if include_special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

# User input asking for data
min_length = int(input("Enter the minimum length: "))
include_numbers = input("Do you want to include numbers (y/n)? ").lower() == "y"
include_special_characters = input("Do you want to include special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, include_numbers, include_special_characters)
print(len(pwd))
print("Your Generated Password is:", pwd)
