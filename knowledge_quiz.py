# IT Knowledge Quiz
# A simple Python quiz about basic IT concepts.

print("=" * 45)
print("IT KNOWLEDGE QUIZ")
print("=" * 45)

# Get the student's name
name = input("Enter your name:")

# Store the quiz questions and answers
questions = [
    {
        "question": "What does IT stand for?",
        "options": [
            "A. Information Technology",
            "B. Internet Tools",
            "C. Information Tools",
            "D. Internet Technology"
        ],
        "answer": "a"
    },
    {
        "question": "Which device is used to type?",
        "options": [
            "A. Monitor",
            "B. Keyboard",
            "C. Printer",
            "D. Speaker"
        ],
        "answer": "b"
    },
    {
        "question": "Which one is a programming language?",
        "options": [
            "A. Python",
            "B. Windows",
            "C. Google",
            "D. Wi-Fi"
        ],
        "answer": "a"
    },
    {
        "question": "Which device shows pictures and text?",
        "options": [
            "A. Mouse",
            "B. Keyboard",
            "C. Monitor",
            "D. Router"
        ],
        "answer": "c"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Power Unit",
            "C. Central Program Unit",
            "D. Computer Processing User"
        ],
        "answer": "a"
    }
]

# Start the score at zero
score = 0

# Go through each question
for question in questions:
    print("\n" + question["question"])
    # Display the answer choices
    for option in question["options"]:
        print(option)
    # Get the student's answer
    answer = input("Your answer:").lower()
    # Check if the answer is correct
    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Calculate and display the final results
print("\n" + "=" * 45)
print("RESULTS")
print("=" * 45)
print(f"Student: {name}")
print(f"Score: {score}/{len(questions)}")
percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")
# Give performance feedback based on the score
if percentage >= 80:
    print("Performance: Excellent!")
elif percentage >= 60:
    print("Performance: Good!")
else:
    print("Performance: Keep practicing!")
print("=" * 45)
