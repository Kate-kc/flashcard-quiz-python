# flashcard-quiz

A Python program to help you memorize vocabulary with flashcards and quizzes.  
This project allows users to load an Excel file of words and their definitions and quiz themselves interactively in the terminal.

---

## Features

- Load vocabulary from an Excel file (`.xlsx`)  
- Quiz yourself on words, definitions, or both  
- Choose the number of questions  
- Randomize question order  
- Track your score and review correct answers  
- Supports multiple languages (e.g., English, French, Chinese)  

---

## Installation

1. Make sure you have Python 3 installed.
2. Install the required Python packages:

```bash
pip install pandas openpyxl
```

---

## Usage

1. **Prepare an Excel file with two columns:**

| Word         | Definition      |
|--------------|----------------|
| pomme  | apple           |
| banane    | banana           |

2. **Run the quiz script:**

```bash
python3 quiz.py
```

3. **Follow the prompts:**

- Enter the Excel file path
- Choose what to display for the questions: Word, Definition, or Both
  - **Word** → the quiz will show the word and you answer with the definition  
  - **Definition** → the quiz will show the definition and you answer with the word  
  - **Both** → each question is randomly either a word or a definition, and you provide the corresponding answer
- Enter the number of questions
- Choose if you want a random order

4. **Answer each question.**
At the end, the program will show your total score and the correct answers.
