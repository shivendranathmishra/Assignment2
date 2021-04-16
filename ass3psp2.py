import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('weight-height.csv')
# convert values to integer to round them
df['Height'] = df['Height'].astype(int)
df['Weight'] = df['Weight'].astype(int)
df.head(3)
weights = df['Weight'].tolist()
plt.hist(weights, bins=20, density=True)
plt.show()
