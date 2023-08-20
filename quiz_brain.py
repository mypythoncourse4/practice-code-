class Quiz_Brain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_have_question(self):
        return self.question_no < len(self.question_list)

    def question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f' Q.{self.question_no} {current_question.text} (True/False)  ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it ")

        else:
            print("wrong answer")
        print(f'write answer is {correct_answer}')
        print(f'your score is {self.score}/ {self.question_no}')
        print("\n")
