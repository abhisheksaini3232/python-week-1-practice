quiz = {
    1: {
        "question": "What is the capital of India?",
        "options": {"a": "Mumbai", "b": "New Delhi", "c": "Kolkata", "d": "Chennai"},
        "answer": "b",
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"},
        "answer": "b",
    },
    3: {
        "question": "Who wrote the National Anthem of India?",
        "options": {
            "a": "Rabindranath Tagore",
            "b": "Mahatma Gandhi",
            "c": "Subhash Chandra Bose",
            "d": "Jawaharlal Nehru",
        },
        "answer": "a",
    },
    4: {
        "question": "Which is the largest ocean on Earth?",
        "options": {
            "a": "Indian Ocean",
            "b": "Atlantic Ocean",
            "c": "Pacific Ocean",
            "d": "Arctic Ocean",
        },
        "answer": "c",
    },
    5: {
        "question": "Which is the national animal of India?",
        "options": {"a": "Lion", "b": "Elephant", "c": "Tiger", "d": "Leopard"},
        "answer": "c",
    },
    6: {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": {"a": "Oxygen", "b": "Carbon Dioxide", "c": "Nitrogen", "d": "Hydrogen"},
        "answer": "b",
    },
    7: {
        "question": "Which is the longest river in the world?",
        "options": {"a": "Nile", "b": "Ganga", "c": "Amazon", "d": "Yangtze"},
        "answer": "a",
    },
    8: {
        "question": "Who invented the telephone?",
        "options": {
            "a": "Albert Einstein",
            "b": "Alexander Graham Bell",
            "c": "Isaac Newton",
            "d": "Nikola Tesla",
        },
        "answer": "b",
    },
    9: {
        "question": "Which is the smallest continent in the world?",
        "options": {"a": "Asia", "b": "Europe", "c": "Australia", "d": "Africa"},
        "answer": "c",
    },
    10: {
        "question": "How many days are there in a leap year?",
        "options": {"a": "364", "b": "365", "c": "366", "d": "367"},
        "answer": "c",
    },
}


def run_quiz(quiz_data: dict):
    score = 0
    total_questions = len(quiz_data)

    print("General Knowledge Quiz")

    for q_no, q_data in quiz_data.items():
        print(f"\nQuestion {q_no}: {q_data['question']}")
        for opt_key, opt_text in q_data["options"].items():
            print(f"  {opt_key}) {opt_text}")

        user_answer = input("Your answer (a/b/c/d): ").strip().lower()

        if user_answer == q_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is '{q_data['answer']}'.")

    print("\nQuiz Finished")
    print(f"Your score: {score} / {total_questions}")

    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent")
    elif percentage >= 70:
        print("Good")
    elif percentage >= 40:
        print("Fair")
    else:
        print("Bed")


if __name__ == "__main__":
    run_quiz(quiz)
