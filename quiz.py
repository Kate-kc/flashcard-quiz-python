import pandas as pd
import random
import unicodedata
import os

def load_data(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path, header=0)
    else:
        df = pd.read_excel(file_path, header=0)

    # Read file, column 1 = Word, column 2 = Definition
    df = df.dropna(how="all")
    print(f"Loaded {len(df)} words") 
    return df

def quiz(df):
    # Choose what to display for the questions
    mode = input("Show (1) Word, (2) Definition, or (3) Both? ")
    while mode not in ["1", "2", "3"]:
        mode = input("Invalid choice. Enter 1, 2, or 3: ")

    # Select the number of questions
    max_q = len(df)
    num_q = input(f"How many questions? (max: {max_q}) ")
    while not num_q.isdigit() or not (1 <= int(num_q) <= max_q):
        num_q = input(f"Please enter a number between 1 and {max_q}: ")
    num_q = int(num_q)

    # Random order?
    random_choice = input("Random order? (y/n): ").lower()
    questions = df.sample(num_q) if random_choice == "y" else df.head(num_q)

    # Start the quiz
    answers = []
    print("\n=== Start Quiz ===\n")
    for idx, row in enumerate(questions.itertuples(index=False), start=1):
        row_list = list(row)
        word, definition = row_list[0], row_list[1]
        if mode == "1":
            q = word
            correct = definition
        elif mode == "2":
            q = definition
            correct = word
        else:
            if random.choice([True, False]):
                q = word
                correct = definition
            else:
                q = definition
                correct = word

        user_answer = input(f"{idx}. {q}\nYour answer: ")
        answers.append((idx, q, user_answer, correct))

    # Check answers
    print("\n=== Results ===")
    score = 0
    for idx, q, user_answer, correct in answers:
        mark = "✔" if user_answer.strip().lower() == str(correct).strip().lower() else "✗"
        if mark == "✔":
            score += 1
        print(f"{mark} | {idx}. {q} | Your Answer: {user_answer} | Correct Answer: {correct} ")

    print(f"\nTotal Score: {score}/{num_q}")

if __name__ == "__main__":
    file_path = input("Enter file path (.xlsx or .csv): ")
    file_path = unicodedata.normalize('NFC', file_path)

    df = load_data(file_path)

    while True:
        quiz(df)
        again = input("\nDo you want to try again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break