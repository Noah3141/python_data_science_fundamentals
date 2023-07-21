import numpy as np


def demonstrate_arrays():
    # Creating NumPy arrays
    array1d = np.array([1, 2, 3, 4, 5])
    array2d = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Displaying arrays
    print("1D Array:")
    print(array1d)
    print("2D Array:")
    # Notice that this prints out automatically in the grid format
    print(array2d)

    # Accessing elements using indexing
    print("\nAccessing elements using indexing:")
    print("First element of array1d:", array1d[0])
    print("Element at row 2, column 1 of array2d:", array2d[1, 0])

    # This shows that index arrays are of form:
    # [second-dimension, first-dimension] which also equates in Python syntax to "outermost array layer > innermost layer" (first, which array, then which element within that array)

    # Slicing arrays
    print("\nSlicing arrays:")
    print("Slice of array1d from index 1 to 3:", array1d[1:4])
    print("Slice of array2d, first two rows, last two columns:")
    # Everything UP to excluding 2-th (3rd) , everything after (including) 1th (2nd)
    print(array2d[:2, 1:])

    # Basic array operations
    print("\nBasic array operations:")
    print("Adding 5 to array1d:", array1d + 5)
    print("Multiplying array2d by 2:")
    print(array2d * 2)

    # Aggregating functions
    print("\nAggregating functions:")
    print("Sum of array1d:", np.sum(array1d))
    print("Mean of array2d:", np.mean(array2d))
    print("Max value in array1d:", np.max(array1d))
    print("Min value in array2d:", np.min(array2d))


if __name__ == "__main__":
    demonstrate_arrays()
