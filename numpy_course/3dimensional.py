import numpy as np


array = np.array([
    [
        [0, 1, 2, 3],
        [6, 16, 62, -10]],
    [
        [24, 1000, 88, 90],
        [1156, 102, 180, 99]]
])

array += 10

mask = np.arange([[0, 10, 1], [0, 10, 1]])

print(array)
print(mask)

%time sum(array)