import matplotlib.pyplot as plt
import statistics
from scipy.stats import gamma
from scipy.stats import poisson
from scipy.stats import binom

l = []
for i in range(10000):
    data = gamma.rvs(a=4, size=10000)
    # data = poisson.rvs(mu=3, size=10000)
    # data = binom.rvs(n=10,p=0.8,size=10000)
    l.append(data.mean())

d_m = statistics.mean(l)
d_std = statistics.stdev(l)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(data, bins='auto')
ax2.hist(l, bins='auto')

print('Media: {:.2f}\nDesvisión típica: {:.2f}'.format(d_m,d_std))
plt.show()
