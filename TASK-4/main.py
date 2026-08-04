def start_quiz():
    score = 0

    print("=== General Knowledge Quiz ===")
    print("Answer the following questions:\n")

    ans1 = input("1. What is the capital of France? ").strip().lower()
    if ans1 == "paris":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer is Paris.\n")

    ans2 = input("2. Which planet is known as the Red Planet? ").strip().lower()
    if ans2 == "mars":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer is Mars.\n")

    ans3 = input("3. What is the largest ocean on Earth? ").strip().lower()
    if ans3 == "pacific" or ans3 == "pacific ocean":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer is Pacific Ocean.\n")

    print("=== Quiz Results ===")
    print(f"Your Final Score: {score}/3")


if __name__ == "__main__":
    start_quiz()
