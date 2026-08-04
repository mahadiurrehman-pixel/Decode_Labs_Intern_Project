import math
import secrets
import string
def generate_password(length):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    password_list = [secrets.choice(char_pool) for _ in range(length)]
    password = "".join(password_list)
    pool_size = len(char_pool)
    entropy = length * math.log2(pool_size)
    return password, entropy
def main():
    print("=== Enterprise Random Password Generator ===")
    try:
        user_input = int(
            input("Enter desired password length (Recommended >= 15): ")
        )
        if user_input < 1:
            print("Error: Length must be greater than 0.")
            return
        password, entropy = generate_password(user_input)
        print("\n--- Generated Credentials ---")
        print(f"Password: {password}")
        print(f"Entropy : {entropy:.2f} bits")
    except ValueError:
        print("Error: Please enter a valid integer for length.")
if __name__ == "__main__":
    main()
