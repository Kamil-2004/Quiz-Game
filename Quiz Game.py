import random

logo = """

 _____ _           _        _____     _        _____               
|   __|_|_____ ___| |___   |     |_ _|_|___   |   __|___ _____ ___ 
|__   | |     | . | | -_|  |  |  | | | |- _|  |  |  | .'|     | -_|
|_____|_|_|_|_|  _|_|___|  |__  _|___|_|___|  |_____|__,|_|_|_|___|
              |_|             |__|


"""
print(logo)

#Simple Quiz Game

import random

def quiz_game():
    print("Welcome to the Simple Quiz Game!\n")
    print("Answer the following questions:\n")

    questions = {
        "Who is the founder of Pakistan?": "Quaid-e-Azam",
        "What is the capital of Pakistan?": "Islamabad",
        "Who is the Prime Minister of Pakistan?": "Imran Khan",
        "Is Pakistan a democratic country?": "Absolutely Not",
        "Which family is the most corrupt in Pakistan?": "Shareef family",
        "What is the currency of Pakistan?": "Rupee",
        "What is the national animal of Pakistan?": "Markhor",
    }
    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    # Ask a random question
    ask_rand_question(questions)

def ask_rand_question(questions):
    random_question = random.choice(list(questions.keys()))
    print(f"\nYour final score is: {score}/{len(questions)}")
    print(f"Random question: {random_question}")

if __name__ == "__main__":
    quiz_game()
  
      
      
      
    
  


































