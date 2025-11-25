import numpy as np
import matplotlib.pyplot as plt
from simulator.rk4 import rk4

g = 9.8
m = 0.1
b = 0.1

t = np.linspace(0, 10, 101)
x0 = np.array([0])


def test(t, x):
    return g - (b / m) * x


x = rk4(test, t, x0)

plt.figure()
plt.plot(t, x)
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.grid()
plt.show()
