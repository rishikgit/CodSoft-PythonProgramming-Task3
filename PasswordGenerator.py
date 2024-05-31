import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
            else:
                password = generate_password(length)
                print("Your generated password is:", password)
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
