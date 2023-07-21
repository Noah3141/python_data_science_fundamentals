import numpy as np


def demonstrate_random_number_generation():
    # Random number generation

    print("Random Array:")
    random_array = np.random.rand(3, 4)  # 3x4 array with random numbers between 0 and 1
    print(random_array)

    print("Random Integer Array:")
    random_int_array = np.random.randint(1, 10, size=(4, 8))  # 2x3 array with random integers between 1 and 10
    print(random_int_array)

    # print("Random Integer 4D Array:")
    # random_int_array4d = np.random.randint(1, 10, size=(4, 4, 3, 5))  # Number of brackets bounds the number of dimensions (a 3d array is bounded by [[[     ]]])
    # print(random_int_array4d)

###
# Examples
# np.random.randint(2, size=10)
# array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
# np.random.randint(1, size=10)
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Generate a 2 x 4 array of ints between 0 and 4, inclusive:

# np.random.randint(5, size=(2, 4))
# array([[4, 0, 2, 1], # random
#        [3, 2, 2, 0]])

# Generate a 1 x 3 array with 3 different upper bounds

# np.random.randint(1, [3, 5, 10])
# array([2, 2, 9]) # random

# Generate a 1 by 3 array with 3 different lower bounds

# np.random.randint([1, 5, 7], 10)
# array([9, 8, 7]) # random

# Generate a 2 by 4 array using broadcasting with dtype of uint8

# np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
# array([[ 8,  6,  9,  7], # random
#        [ 1, 16,  9, 12]], dtype=uint8)
# ------------------------------
# randint(low, high=None, size=None, dtype=int)
# Return random integers from low (inclusive) to high (exclusive).

# Return random integers from the "discrete uniform" distribution of the specified dtype in the "half-open" interval [low, high). If high is None (the default), then results are from [0, low).


def demonstrate_array_broadcasting():
    # Array broadcasting
    array1 = np.array([[1, 2, 3]])  # 1d row
    array2 = np.array([[10], [20]])  # 1d col

    # Broadcasting array1 and array2 to perform element-wise multiplication
    result_array = array1 * array2  # results in 2d array

    print("Array1:")
    print(array1)
    print("Array2:")
    print(array2)
    print("Result Array (after broadcasting):")
    print(result_array)
    print("\n============================================\n\n")


def demonstrate_array_aggregation():
    # Array aggregation and statistical operations
    # 3x3 in col by row
    array = np.array([
        [1, 2, 3],
        [1, 2, 3],
        [25, 5, 6],
        [7, 8, 9]
    ])
    print(f"The 25 is located at 2th row, 0th col: array3d[2, 0] = {array[2, 0]}")
    print("row-col")
    print("0   1 ")
    # Aggregating functions
    col_sums = np.sum(array, axis=0)
    row_sums = np.sum(array, axis=1)
    overall_max = np.max(array)
    overall_min = np.min(array)

    print("Array:")
    print(array)

    print("Row Sums (axis 1 - indexing col-wise):")
    print("To sum along rows, we get a value for each col")
    print(row_sums)

    print("Column Sums (axis 0 - indexing row-wise):")
    print("To sum along cols, we get a value for each row")
    print(col_sums)

    print("Overall Max Value:")
    print(overall_max)
    print("Overall Min Value:")
    print(overall_min)
    print("\n~\n")

    # Let's do all that again but with a more complex array:
    # 3x4 in col by row, but 2 of them, so 2x3x4
    array3d = np.array([
        [
            [1, 1, 1],  # 2 dimensional array with 3 col 4 row
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]],
        [
            [3, 3, 3],  # Another 2 dimensional, making 3D (third dimension picks which 2D)
            [4, 4, 4],
            [25, 5, 5],
            [3, 3, 3]]
    ])

    print(f"The 25 is located at 1th depth, 2th row, 0th col: array3d[1, 2, 0] = {array3d[1, 2, 0]}")
    print("dep-row-col")
    print("0   1   2")
    multid_zeroth_sums = np.sum(array3d, axis=0)
    multid_oneth_sums = np.sum(array3d, axis=1)
    multid_twoth_sums = np.sum(array3d, axis=2)
    multid_overall_max = np.max(array3d)
    multid_overall_min = np.min(array3d)
    print("\nTo sum the rows of a cube, we mean to sum the row at one depth, and to separately sum the row at adjacent depth. We are only summing the cells in one line; since 3D arrays give 2 dimensions along which to draw that line, meaning 2D outputs.")

    print("\n3D Array:")
    print("\n--------------------")
    print(array3d)
    print("\n--------------------")

    print("Depth Sums (axis 0 - indexing outermost):")
    print("To sum along depths, we look at the cube and stab along the depth axis for every row-col pair")
    print(multid_zeroth_sums)

    print("When we 'sum across axis 1', we mean to take an item from each index in 1, which is technically rows. When we span across all the items in a row, we get a column. So it is called a column sum, by addressing across the row axis.")
    print("\nRows Sum (axis 2 - index cols):")
    print("To sum along rows, we get a value for each depth & col")
    print(multid_twoth_sums)

    print("\nCols Sums (axis 1 - indexing rows:")
    print("To sum along cols, we get a value for each depth & row")
    print(multid_oneth_sums)

    print("Altogether, to sum columns we ")

    print("\n\nOverall Max Value:")
    print(multid_overall_max)
    print("Overall Min Value:")
    print(multid_overall_min)

    print("\n~\n")


if __name__ == "__main__":
    print("Demonstrating Random Number Generation:")
    demonstrate_random_number_generation()

    print("\nDemonstrating Array Broadcasting:")
    demonstrate_array_broadcasting()

    print("\nDemonstrating Array Aggregation:")
    demonstrate_array_aggregation()
