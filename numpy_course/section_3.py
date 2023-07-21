import numpy as np


def demonstrate_random_number_generation():
    # Random number generation
    random_array = np.random.rand(3, 4)  # 3x4 array with random numbers between 0 and 1
    random_int_array = np.random.randint(1, 10, size=(2, 3))  # 2x3 array with random integers between 1 and 10

    print("Random Array:")
    print(random_array)
    print("Random Integer Array:")
    print(random_int_array)


def demonstrate_array_broadcasting():
    # Array broadcasting
    array1 = np.array([[1, 2, 3]])
    array2 = np.array([[10], [20]])

    # Broadcasting array1 and array2 to perform element-wise multiplication
    result_array = array1 * array2

    print("Array1:")
    print(array1)
    print("Array2:")
    print(array2)
    print("Result Array (after broadcasting):")
    print(result_array)


def demonstrate_array_aggregation():
    # Array aggregation and statistical operations
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Aggregating functions
    row_sums = np.sum(array, axis=1)
    col_means = np.mean(array, axis=0)
    overall_max = np.max(array)
    overall_min = np.min(array)

    print("Array:")
    print(array)
    print("Row Sums:")
    print(row_sums)
    print("Column Means:")
    print(col_means)
    print("Overall Max Value:")
    print(overall_max)
    print("Overall Min Value:")
    print(overall_min)


if __name__ == "__main__":
    print("Demonstrating Random Number Generation:")
    demonstrate_random_number_generation()

    print("\nDemonstrating Array Broadcasting:")
    demonstrate_array_broadcasting()

    print("\nDemonstrating Array Aggregation:")
    demonstrate_array_aggregation()
