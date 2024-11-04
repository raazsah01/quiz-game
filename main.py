# Define a dictionary of questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our Solar System?": "Jupiter",
    "How many continents are there on Earth?": "7",
    "What is the square root of 64?": "8",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare"
}

# Function to run the quiz
def run_quiz():
    score = 0
    total_questions = len(quiz_questions)

    print("Welcome to the Quiz Game!")
    print("Answer the questions below:\n")

    for question, correct_answer in quiz_questions.items():
        # Ask the question and get the user's answer
        user_answer = input(f"{question} ")

        # Check if the answer is correct
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

        print()  # Print a blank line for spacing

    # Final score
    print(f"You scored {score} out of {total_questions}.")
    if score == total_questions:
        print("Excellent! You got all questions right!")
    elif score >= total_questions / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time.")

# Run the quiz
run_quiz()
