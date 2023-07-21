import numpy as np

# Array sorting and searching
array = np.array([
    [5, 2, 9, 1, 5, 3],
    [7, 2, 9, 1, 5, 9],
    [2, 2, 4, 1, 2, 8],
])


print("Original Array:")
print(array)


# # Sorting the array
# sorted_array = np.sort(array, axis=0)
# print("Sorted Array:")
# print(sorted_array)

# Finding the index of a specific value
value_to_search = 5
index = np.where(array == value_to_search)
print(index)

matrix_index = np.vstack((index[0], index[1]))

print(f"Concatenated: \n{matrix_index}")

print("Indexing using the where:".format(value_to_search))
print(array[index])


print("Changing all 5's to 3's")
array[np.where(array == 5)] -= 3


print(array)
