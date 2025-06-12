import random
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def generate_random_floats(length: int = 1000, range_upper: int = 5000):
    """
    Generate a list of random floats between 0 and 5000. 

    Parameters:
    length (int): The number of random floats to generate.

    Returns:
    list: A list of random float numbers.
    """
    return [random.uniform(0, range_upper) for _ in range(length)]


def visualize_normal_distribution(values: list = [], title: str = "Histogram with KDE"):
    """
    Visualize whether a list of numerical values follows a normal distribution
    using both a histogram with KDE and a Q-Q plot.

    Parameters:
    values (list): A list of numerical values.

    Returns:
    None
    """
    if not values:
        raise ValueError("The list of values is empty. Please provide a list of numerical values.")
    # Sort the values
    values.sort()

    # Create a figure with two subplots
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Histogram with KDE
    sns.histplot(values, kde=True, ax=ax[0])
    ax[0].set_title(title)
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')

    # Q-Q plot
    stats.probplot(values, dist="norm", plot=ax[1])
    ax[1].set_title('Q-Q Plot')

    # Show the plots
    plt.tight_layout()
    plt.show()