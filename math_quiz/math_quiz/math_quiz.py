import random

def generate_random_int(min_value, max_value):
    """
    Generate a random integer between the specified min and max values.
    
    Args:
        min_value (int): The minimum value for the random number.
        max_value (int): The maximum value for the random number.
        
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_operator():
    """
    Randomly select a mathematical operator (+, -, or *).
    
    Returns:
        str: A random operator as a string.
    """
    return random.choice(['+', '-', '*'])


def create_problem_and_solution(num1, num2, operator):
    """
    Create a math problem as a string and calculate the solution.
    
    Args:
        num1 (int): The first number for the problem.
        num2 (int): The second number for the problem.
        operator (str): The operator to be used (+, -, or *).
        
    Returns:
        tuple: A tuple containing the problem as a string and the solution as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    else:  # operator == '*'
        solution = num1 * num2
    
    return problem, solution


def math_quiz():
    """
    Main function to run the math quiz game. The user is prompted with math problems, 
    and their answers are evaluated.
    
    The game ends after 5 questions, and the user’s score is displayed.
    """
    score = 0
    total_questions = 5  # Total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_int(1, 10)
        num2 = generate_random_int(1, 5)  # Ensure num2 is an integer
        operator = choose_operator()

        # Generate problem and solution
        problem, correct_answer = create_problem_and_solution(num1, num2, operator)

        print(f"\nQuestion: {problem}")

        # Handle user input and validate it
        while True:
            try:
                user_answer = input("Your answer: ")

                # Attempt to convert the user input to an integer
                user_answer = int(user_answer)

                # Compare the user's answer with the correct answer
                if user_answer == correct_answer:
                    print("Correct! You earned a point.")
                    score += 1
                else:
                    print(f"Wrong answer. The correct answer is {correct_answer}.")
                break  # Exit the input loop after a valid answer

            except ValueError:
                # Handle case where the user input is not a valid integer
                print("Invalid input! Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
