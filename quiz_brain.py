class Quiz_Brain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {question}? (True or false) ")
        self.check_answer(answer)

    def check_answer(self, ans):
        answer = self.question_list[self.question_number - 1].answer
        if ans.lower() == answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {answer}.")
        print(f"you score is {self.score}/{self.question_number}.")
        print('\n')

    def final_score(self):
        return f"Your final score is {self.score}/{self.question_number}."
