from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain

question_bank = []
for qa_dict in question_data:
    text = qa_dict['question']
    answer = qa_dict['correct_answer']
    q = Question(text, answer)
    question_bank.append(q)

quiz = Quiz_Brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You're completing the quiz.")
finalscore = quiz.final_score()
print(finalscore)
