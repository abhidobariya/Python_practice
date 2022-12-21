import numpy as np
import pandas as pd

# empty_series = pd.Series()
# print(empty_series())

my_list = [10,20,30]
series1 = pd.Series(my_list)
print(type(series1))
print(series1)

pd.Series(my_list, index= ['a', 'ABC','&'])



