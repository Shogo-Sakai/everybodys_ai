import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)

# y = 2^x
y_2 = 2**x

# y = 3^x
y_3 = 3**x

print (x)
print (y_2)

plt.plot(x, y_2)
plt.plot(x, y_3)
plt.show()

