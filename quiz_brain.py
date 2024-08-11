
class QuizBrain:
    def  __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def still_has_questions(self):
        if self.question_number>=len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q.{self.question_number} {question.text} (True/False)?")
        self.check_answer(ans,question.answer)


    def check_answer(self,ans,question_answer):
        if ans.lower()==question_answer.lower():
            print("you are right")
            self.score+=1
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer is {question_answer}")
        print("\n")


