from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
final_score = 0
ques_number = 0
for ques in question_data:
    question = Question(ques["question"], ques["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_ques()

while quiz.still_has_ques():
    quiz.next_ques()

print("You've  completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
