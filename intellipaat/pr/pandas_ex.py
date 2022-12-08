import pandas as pd
import numpy as np

ser1 = pd.series[1,2,3,4], index = ["USA","Germany","USSR","Japan"]
print(ser1)


ser2 = pd.series[1,2,3,4], index = ["USA","Germany","Itali","Japan"]
print(ser2)


#practice que
df = pd.DataFrame()
print(df)
print(type(df))

df = pd.DataFrame(np.random.rand(4,4))
print(df)