import random
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def generate_random_floats(length: int = 1000):
    """
    Generate a list of random floats between 0 and 3000.

    Parameters:
    length (int): The number of random floats to generate.

    Returns:
    list: A list of random float numbers.
    """
    return [random.uniform(0, 3000) for _ in range(length)]


def visualize_normal_distribution(values):
    """
    Visualize whether a list of numerical values follows a normal distribution
    using both a histogram with KDE and a Q-Q plot.

    Parameters:
    values (list): A list of numerical values.

    Returns:
    None
    """
    # Sort the values
    values.sort()

    # Create a figure with two subplots
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Histogram with KDE
    sns.histplot(values, kde=True, ax=ax[0])
    ax[0].set_title('Histogram with KDE')
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')

    # Q-Q plot
    stats.probplot(values, dist="norm", plot=ax[1])
    ax[1].set_title('Q-Q Plot')

    # Show the plots
    plt.tight_layout()
    plt.show()