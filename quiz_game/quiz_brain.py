import textwrap


class Quiz_Brain:
    def __init__(self, question_bank):
        self.right_or_wrong = None
        self.flag = 0
        self.user_input = None
        self.question_number = 0
        self.score = 0
        print(question_bank)
        self.question_bank = question_bank
        self.user_choice = ''

    def next_question(self):
        qb = self.question_UI()
        self.question_number += 1
        self.correct_answer(qb, self.user_input)

    def question_UI(self):
        qb = self.question_bank[self.question_number - 1]
        print(qb.text)
        return qb

    def user_Choice(self, choice):
        self.user_input = choice
        self.next_question()

    def wrap_text(self):
        qb = self.question_UI()

        x = textwrap.wrap(qb.text, 20)

        return x

    def when_to_exit(self):
        # print(f"Your Score is : {self.score} /{self.question_number}")
        return self.question_number < len(self.question_bank)

    def correct_answer(self, quest_ans, user_choice):
        if (user_choice == "t" and quest_ans.answer == "True") or (user_choice == "f" and quest_ans.answer == "False"):
            print("Your are correct. ")

            self.score += 1
            self.right_or_wrong = True
        else:
            print("you are wrong")
            self.right_or_wrong = False

    def get_final_score(self):
        print(f"Your Score is : {self.score} /{self.question_number}")

        return self.score

    def get_question_number(self):

        return str(self.question_number + 1)
