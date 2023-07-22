import numpy as np


def linspace_example():
    # Creating a linearly spaced array from 0 to 10 with 5 elements
    linear_array = np.linspace(0, 10, 5)
    print("Linearly spaced array with 5 elements:")
    print(linear_array)

    # Creating a linearly spaced array from -5 to 5 with 11 elements
    linear_array2 = np.linspace(-5, 5, 11)
    print("\nLinearly spaced array with 11 elements:")
    print(linear_array2)

    # Creating a linearly spaced array from 1 to 100 with 20 elements
    linear_array3 = np.linspace(1, 100, 20)
    print("\nLinearly spaced array with 20 elements:")
    print(linear_array3)

    # Using the retstep parameter to get the step value
    linear_array4, step = np.linspace(0, 10, 5, retstep=True)
    print("\nLinearly spaced array with step value:")
    print("Array:", linear_array4)
    print("Step value:", step)


if __name__ == "__main__":
    linspace_example()
