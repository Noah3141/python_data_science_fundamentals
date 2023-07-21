import numpy as np


def demonstrate_array_manipulation():
    # Reshaping arrays
    array1d = np.array([1, 2, 3, 4, 5, 6])
    reshaped_array = array1d.reshape(2, 3)

    print("Original 1D Array:")
    print(array1d)
    print("Reshaped 2D Array:")
    print(reshaped_array)

    # Concatenating arrays
    array1 = np.array([
        [1, 2],
        [3, 4]
    ])

    # Option 1 #
    # array2 = np.array([[5, 6]])
    # concatenated_array = np.concatenate((array1, array2), axis=0)

    # Option 2 #
    array2 = np.array([[0, 0], [5, 6]])
    concatenated_array = np.concatenate((array1, array2), axis=1)

    print("\n~\n")

    print("\nArray 1:")
    print(array1)
    print("Array 2:")
    print(array2)
    print("Concatenated Array:")
    print(concatenated_array)

    print("\n~\n")

    # Splitting arrays
    array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    split_arrays = np.split(array3, indices_or_sections=3, axis=0)

    print("\nOriginal Array:")
    print(array3)
    print("Split Arrays:")
    print(split_arrays)

    print("\n~\n")


def demonstrate_universal_functions():
    # Universal functions (ufuncs)
    array = np.array([1, 2, 3, 4, 5])

    # Element-wise operations using ufuncs
    squared_array = np.square(array)
    sqrt_array = np.sqrt(array)
    exp_array = np.exp(array)

    print("\nOriginal Array:")
    print(array)
    print("Squared Array:")
    print(squared_array)
    print("Square Root Array:")
    print(sqrt_array)
    print("Exponential Array:")
    print(exp_array)


if __name__ == "__main__":
    print("Demonstrating Array Manipulation:")
    demonstrate_array_manipulation()

    print("\nDemonstrating Universal Functions:")
    demonstrate_universal_functions()
