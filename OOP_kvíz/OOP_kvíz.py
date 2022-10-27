from quesion_model import Question
from question_data import question_data
from quiz_brain import QuizBrain
question_list = []

for one_question in question_data:
    question_text = (one_question["question"])
    question_answer = (one_question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)


quiz = QuizBrain(question_list)
while quiz.any_questions():
    quiz.next_question()

print(f"Dokončili jste qvíz se score {quiz.score} z {quiz.question_number} otázek.")
