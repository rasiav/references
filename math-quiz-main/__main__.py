import random

def generate_harmonic_sequence(length):
    # Generate a random starting value (a) and common difference (d) for the arithmetic sequence
    a = random.randint(1, 10)  # Starting value between 1 and 10
    d = random.randint(1, 5)   # Common difference between 1 and 5

    arithmetic_sequence = []
    harmonic_sequence = []

    # Create the arithmetic sequence and corresponding harmonic sequence
    for i in range(length):
        term = a + i * d
        arithmetic_sequence.append(term)
        harmonic_sequence.append(f"1/{term}")

    return harmonic_sequence

def harmonic_sequence_quiz():
    sequence_length = 4  # Number of terms to show to the user
    harmonic_sequence = generate_harmonic_sequence(sequence_length + 1)

    # Display the harmonic sequence as a string (except the last term)
    print("Harmonic Sequence:", ", ".join(harmonic_sequence[:-1]))

    # Prompt the user to guess the next term in the sequence
    user_answer = input("What should come next in the sequence? Enter as '1/number': ")

    # Check if the user's answer matches the next term
    correct_answer = harmonic_sequence[-1]
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was {correct_answer}.")

# Run the quiz
harmonic_sequence_quiz()
