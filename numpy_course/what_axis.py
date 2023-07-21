import numpy as np


# array = np.array([
#     [
#         [
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#         ],
#         [
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5]
#         ],
#         [
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#         ]],
#     [
#         [
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#         ],
#         [
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5]

#         ],
#         [
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5],
#             [1, 2, 3, 4, 5]

#         ],

#     ]])

# array = np.array(
#     [
#         [
#             [0, 1, 2, 3, 4, 5],
#             [0, 1, 2, 3, 4, 5],
#             [0, 1, 2, 3, 4, 5],
#         ],
#         [
#             [0, 1, 2, 3, 4, 5],
#             [0, 1, 2, 3, 4, 5],
#             [0, 1, 2, 3, 4, 5],
#         ],
#     ])
array = np.array(
    [0, 1, 2, 3, 4, 5],
)

print("Array:")
print(array)
print("\n\n")
negoneth_sums = np.sum(array, axis=-1)
print("-1 Sums:")
print(negoneth_sums)

print("\n")

zeroth_sums = np.sum(array, axis=0)
print("0 Sums:")
print(zeroth_sums)

print("\n")

# oneth_sums = np.sum(array, axis=1)
# print("1 Sums:")
# print(oneth_sums)

print("\n")

# twoth_sums = np.sum(array, axis=2)
# print("2 Sums:")
# print(twoth_sums)

print("\n")

# threeth_sums = np.sum(array, axis=3)
# print("3 Sums:")
# print(threeth_sums)
