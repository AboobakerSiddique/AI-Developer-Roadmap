print("Welcome to the Quiz App!")
print("------------------------------")

question_bank = [
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], "answer": "A"},
    {"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "answer": "B"},
    {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"], "answer": "D"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"], "answer": "A"},
    {"question": "What is the chemical symbol for water?", "options": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"], "answer": "A"},
    {"question": "What is the speed of light?", "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 100,000 km/s", "D. 50,000 km/s"], "answer": "A"},
    {"question": "What is the largest planet in our solar system?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": "C"},
    {"question": "What is the smallest prime number?", "options": ["A. 0", "B. 1", "C. 2", "D. 3"], "answer": "C"},
    {"question": "What is the boiling point of water?", "options": ["A. 100°C", "B. 90°C", "C. 80°C", "D. 70°C"], "answer": "A"},
    {"question": "What is the largest mammal on Earth?", "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"], "answer": "B"}
]


def start_quiz():
    score = 0

    for i, question in enumerate(question_bank, start=1):
        print(f"\nQuestion {i}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (A, B, C, D): ").upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Please enter only A, B, C or D.")

        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {question['answer']}")

    print(f"\n🎉 Your final score is: {score}/{len(question_bank)}")
    return score


def view_score():
    try:
        with open("score.txt", "r") as file:
            score = file.read()
            print(f"\nYour last score was: {score}")
    except FileNotFoundError:
        print("No score recorded yet.")


def save_score(score):
    with open("score.txt", "w") as file:
        file.write(f"{score}/{len(question_bank)}")


while True:

    print("\n------------------------------")
    print("1. Start Quiz")
    print("2. View Score")
    print("3. Exit")
    print("------------------------------")

    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            score = start_quiz()
            save_score(score)

        elif choice == 2:
            view_score()

        elif choice == 3:
            print("Exiting the Quiz App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    except ValueError:
        print("Please enter numbers only.")