class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list1 = q_list

    def next_question(self):
        current_question = self.question_list1[self.question_number]
        self.question_number += 1
        user_answer = input(f"Otázka číslo {self.question_number}: {current_question.text} (true/false): ")
        self.checker(user_answer, current_question.answer)

    def checker(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print(f"Správně")
            self.score += 1
        else:
            print(f"Špatně, správně bylo {correct_answer}")
        print(f"Soušasné score je {self.score} z {self.question_number} otázek.")

    def any_questions(self):
        if self.question_number < len(self.question_list1):
            return True
        else:
            return False


