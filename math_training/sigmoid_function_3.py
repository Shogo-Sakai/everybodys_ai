import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(a):
    s = 1 / (1 + e**-a)
    return s

def d_sigmoid(a):
    d = sigmoid(a) * (1 - sigmoid(x))
    return d

e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# シグモイド関数 y = 1 / ( 1 + e^(-x))
y_sig = sigmoid(x)
# シグモイド関数の傾きの微分
y_dsig = (sigmoid(x+dx) - sigmoid(x)) / dx
# シグモイド関数の微分
dy_sig = d_sigmoid(x)

plt.plot(x, y_sig,  label = "sigomid")
plt.plot(x, y_dsig, label = "d_sigmoid")
plt.plot(x, dy_sig, label = "dy_sigmoid")
plt.legend()
plt.show()

