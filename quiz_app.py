def display_question(question, options):
    print(f"\n{question}")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

def get_user_answer(options):
    while True:
        answer = input("Enter the number of your answer or the name of the city: ").strip()
        if answer.isdigit():
            return int(answer)
        elif answer in options:
            return options.index(answer) + 1
        else:
            print("Please enter a valid number or city name.")

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 4
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
            "answer": 3
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": 1
        }
    ]

    score = 0

    for question in questions:
        display_question(question["question"], question["options"])
        user_answer = get_user_answer(question["options"])

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {question['options'][question['answer'] - 1]}")

    print(f"\nYour final score is: {score}/{len(questions)}")

    if input("Do you want to retake the quiz? (yes/no): ").lower() == 'yes':
        main()

if __name__ == "__main__":
    main()
