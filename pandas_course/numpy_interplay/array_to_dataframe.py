import numpy as np
import pandas as pd

array = np.random.uniform(0, 100, 15)  # , (10, 10, 10)

series = pd.Series(array)


print(array)
print("\n\n")
print(series)
