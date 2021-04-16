import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean,std
from scipy.stats import norm

df = pd.read_csv('weight-height.csv')
df.head(3)

df = df[df['Gender']=='Female']
df.head(3)
weights = df['Weight'].tolist()
#plt.hist(weights, bins=20)

mean = mean(weights)
std = std(weights)
print(mean, std)

distribution = norm(mean, std)

min_weight = min(weights)
max_weight = max(weights)
values = list(range(int(min_weight), int(max_weight)))

probabilities = [distribution.pdf(v) for v in values]

plt.hist(weights, bins=20, density=True) # , 
plt.plot(values, probabilities)
plt.show()
