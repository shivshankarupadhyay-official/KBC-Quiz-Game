questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who is the current Prime Minister of India?",
        "options": ["A. Rahul Gandhi", "B. Arvind Kejriwal", "C. Narendra Modi", "D. Amit Shah"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Mahatma Gandhi", "D. Subhash Chandra Bose"],
        "answer": "A"
    }
]

prize_money = [1000, 5000, 10000, 50000]
total_prize = 0

print("🎉 Welcome to 'Kaun Banega Crorepati' 🎉")
print("---------------------------------------")

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q['options']:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == q['answer']:
        total_prize = prize_money[i]
        print(f"✅ Correct! You have won ₹{total_prize}")
    else:
        print("❌ Wrong answer!")
        print(f"💰 You won ₹{total_prize}")
        break

print("\n🙏 Thank you for playing Kaun Banega Crorepati!")

