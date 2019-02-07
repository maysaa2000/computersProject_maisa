import matplotlib.pyplot as plt
import numpy as np

x = [-1, -2, -3, -4, 6, 7, 7.1]
y = [7.2, 8.3, 9.1, 9.9, 0.2, -1, -1.05]
dx = [0.01, 0.01, 0.02, 0.04, 0.01, 0.02, 0.02]
dy = [0.2, 0.1, 0.3, 0.1, 0.11, 0.02, 0.2]
a = -1.0090838562081268
b = 6.071382393439187
def plot (x,y,dx,dy,a,b):
    error = plt.errorbar(x, y, dx, dy, '|')
    plt.setp(error, color='b', linewidth=2.0, )

    yfit = [b + a * xi for xi in x]
    line = plt.plot(x, yfit)
    plt.setp(line, color='r', linewidth=2.0, )
    plt.show()



