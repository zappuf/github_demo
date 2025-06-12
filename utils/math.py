import random

def generate_random_floats(length: int = 1000):
    """
    Generate a list of random floats between 0 and 3000.

    Parameters:
    length (int): The number of random floats to generate.

    Returns:
    list: A list of random float numbers.
    """
    return [random.uniform(0, 3000) for _ in range(length)]
