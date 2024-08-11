from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for item in question_data:
    q=item["question"]
    ans=item["correct_answer"]
    new_q=Question(q,ans)
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You Completed the quiz")
    print(f"Your final score is {quiz.score}/{quiz.question_number}")



