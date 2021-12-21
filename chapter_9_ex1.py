# maximum likelihood estimation

import numpy as np
import math
from matplotlib import pyplot as plt

p = np.linspace(0.4,0.8,50)
n = 100
k = 56
nCk = lambda p : math.factorial(n)/(math.factorial(k)*math.factorial(n-k))*p**k*(1-p)**(n-k)
likelihood_f = [nCk(p_) for p_ in p]

plt.plot(p,likelihood_f,'b-',label="my mine")
plt.xlabel('p')
plt.ylabel('ML_f')
plt.legend()
plt.show()