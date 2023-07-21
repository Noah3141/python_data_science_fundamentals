import numpy as np


def demonstrate_array_sorting_and_searching():
    # Array sorting and searching
    array = np.array([5, 2, 9, 1, 5, 3])
    print("Original Array:")
    print(array)

    # Sorting the array
    sorted_array = np.sort(array)
    print("Sorted Array:")
    print(sorted_array)

    # Finding the index of a specific value
    value_to_search = 5
    index = np.where(array == value_to_search)
    print("Index of value {} in the original array:".format(value_to_search))
    print(index[0])  # Since np.where() returns a tuple, we access the first element


def demonstrate_file_input_output():
    # File input/output
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Saving the array to a file
    np.save("saved_array.npy", array)

    # Loading the array from the file
    loaded_array = np.load("saved_array.npy")

    print("Original Array:")
    print(array)
    print("Loaded Array:")
    print(loaded_array)


def demonstrate_additional_concepts():
    # Additional concepts and advanced features
    array = np.array([1, 2, 3, 4, 5])

    # Advanced indexing
    boolean_mask = array > 2
    selected_elements = array[boolean_mask]

    print("Original Array:")
    print(array)
    print("Boolean Mask:")
    print(boolean_mask)
    print("Selected Elements using Boolean Mask:")
    print(selected_elements)


if __name__ == "__main__":
    print("Demonstrating Array Sorting and Searching:")
    demonstrate_array_sorting_and_searching()

    print("\nDemonstrating File Input/Output:")
    demonstrate_file_input_output()

    print("\nDemonstrating Additional Concepts:")
    demonstrate_additional_concepts()
