import random
import string

def generate_strong_password(length=12):
    """
    Generates a strong password with a mix of uppercase, lowercase,
    digits, and special characters.
    """
    if length < 8:
        print("Password length should be at least 8 characters for stronger security.")
        length = 8

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each set is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length
    all_chars = lowercase + uppercase + digits + special_chars
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    # Shuffle the password list to randomize character positions
    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    try:
        password_length = int(input("Enter desired password length (min 8): "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        password_length = 12

    strong_pass = generate_strong_password(password_length)
    print(f"\nGenerated Strong Password: {strong_pass}")
    print("Remember to store your password safely!")
