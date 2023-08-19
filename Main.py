import random

class MathQuizGame:
    def __init__(self):
        self.score = 0
    
    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*', '/'])
        question = f"What is {num1} {operator} {num2}?"
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        else:
            answer = num1 / num2
            answer = round(answer, 2)  # Round to 2 decimal places for division
        return question, answer
    
    def play(self, num_questions=20):
        for _ in range(num_questions):
            question, correct_answer = self.generate_question()
            print(question)
            user_answer = float(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong. The correct answer was {correct_answer}.\n")
        print(f"Your final score: {self.score}/{num_questions}")

# Create and play the game with 20 questions
game = MathQuizGame()
game.play(num_questions=20)
