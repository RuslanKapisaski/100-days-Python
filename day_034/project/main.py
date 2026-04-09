from question_model import Question
from data import questions
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in questions:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
QuizInterface(quiz)
