import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Defining the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all character sets
    all_characters = lowercase + uppercase + numbers + special_chars

    # Ensure that the password contains at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get user preferences for password complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()