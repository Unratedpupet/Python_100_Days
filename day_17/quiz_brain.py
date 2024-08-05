#TODO: Ask the questions
#TODO: Check if answer is correct
#TODO: Check if at end of quiz
from question_model import Question


class QuizBrain:

    def __init__(self, question_list: list[Question]) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self) -> bool:
        """Checks to see if there are still questions to be asked by comparing the length of the quiz bank to the current question number.

        Returns:
            bool: The T/F response to whether there are still questions to be asked.
        """
        return len(self.question_list) > self.question_number

    def next_question(self) -> str:
        """Asks the next question by initializing the first question, incrementing, then asking.

        Returns:
            str: The answer to the question asked.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text}? True/False: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("That is correct!")
            self.score += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}.\n")