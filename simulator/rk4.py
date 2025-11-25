import numpy as np


def rk4(func, t, x0):
    n = len(t)
    x = np.zeros(n)
    x[0] = x0

    dt = (t[-1] - t[0]) / (n - 1)

    for i in range(n - 1):
        x[i + 1] = rk4_step(func, t[i], x[i], dt)

    return x


def rk4_step(func, t, x, dt):
    k1 = func(t, x)
    k2 = func(t + dt / 2, x + dt * k1 / 2)
    k3 = func(t + dt / 2, x + dt * k2 / 2)
    k4 = func(t + dt, x + dt * k3)

    return x + (dt / 6) * (k1 + k2 / 2 + k3 / 2 + k4)
