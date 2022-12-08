import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y = 2*x+5

print(x)
print(y)

plt.plot(x , y)

plt.plot(x,y,color = 'r')

plt.figure(figsize=(5,5))
plt.plot(x,y)

plt.plot(x,y,color = 'r')

plt.figure(figsize=(2,2))
plt.plot(x,y)

plt.plot(x,y)
plt.title('Line chart Demo')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
