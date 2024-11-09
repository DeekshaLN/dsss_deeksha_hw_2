import unittest
from unittest.mock import patch
import random

# Import the functions from your math_quiz.py
from math_quiz import generate_random_int, choose_operator, create_problem_and_solution


class TestMathQuizFunctions(unittest.TestCase):

    # Test generate_random_int() with fixed min and max range
    @patch('random.randint')
    def test_generate_random_int(self, mock_randint):
        # Set up the mock to return a specific value
        mock_randint.return_value = 7
        result = generate_random_int(1, 10)
        self.assertEqual(result, 7)  # Check if the mocked value is returned

        # Test another case
        mock_randint.return_value = 3
        result = generate_random_int(1, 5)
        self.assertEqual(result, 3)

    # Test choose_operator() for random operator selection
    @patch('random.choice')
    def test_choose_operator(self, mock_choice):
        # Mock the return value to simulate the operator being chosen
        mock_choice.return_value = "+"
        result = choose_operator()
        self.assertEqual(result, "+")  # Check if the chosen operator is '+'

        # Test other possible return values
        mock_choice.return_value = "-"
        result = choose_operator()
        self.assertEqual(result, "-")

        mock_choice.return_value = "*"
        result = choose_operator()
        self.assertEqual(result, "*")

    # Test create_problem_and_solution() to verify problem creation and solution calculation
    def test_create_problem_and_solution(self):
        # Test case for addition
        problem, solution = create_problem_and_solution(3, 2, "+")
        self.assertEqual(problem, "3 + 2")
        self.assertEqual(solution, 5)

        # Test case for subtraction
        problem, solution = create_problem_and_solution(5, 3, "-")
        self.assertEqual(problem, "5 - 3")
        self.assertEqual(solution, 2)

        # Test case for multiplication
        problem, solution = create_problem_and_solution(4, 6, "*")
        self.assertEqual(problem, "4 * 6")
        self.assertEqual(solution, 24)

    # Test user input handling for math_quiz() (Simulate user input and check output)
    @patch('builtins.input', side_effect=["5", "4", "12", "10", "20"])  # Simulate user input
    def test_math_quiz(self, mock_input):
        with patch('builtins.print') as mock_print:  # Mock print to avoid actual output
            # Simulate math quiz, we'll just verify the score at the end
            with patch('random.randint', side_effect=[3, 2, 5, 4, 7]):  # Simulate fixed random numbers
                with patch('random.choice', side_effect=['+', '-', '*', '+', '-']):
                    math_quiz()

            # Check if the score is printed
            mock_print.assert_any_call("Game over! Your score is: 3/5")  # Adjust based on mock input

if __name__ == '__main__':
    unittest.main()
