import numpy as np
import matplotlib.pyplot as plt

# Constraints
x = np.linspace(0, 50, 100)

y1 = (200 - 5*x)/4
y2 = (150 - 3*x)/5
y3 = (100 - 5*x)/4
y4 = (80 - 8*x)/4
y5 = x*0

plt.plot(x, y5, label='y >= 0') # x-axis
plt.plot(y5, x, label='x >= 0') # y-axis
plt.plot(x, y1, label='5x + 4y <= 200')
plt.plot(x, y2, label='3x + 5y <= 150')
plt.plot(x, y3, label='5x + 4y >= 100')
plt.plot(x, y4, label='8x + 4y >= 80')
plt.xlabel('coordinates')
plt.ylabel('abcissa')
plt.legend()
plt.xlim(-1, 51)
plt.ylim(-1, 51)


up = np.minimum(y1, y2)
lo = np.maximum(y3, y4)
lo = np.maximum(lo, y5)
plt.fill_between(x, up, lo, where= up>lo, color='grey', alpha=0.5)

plt.show()

def intersection(a, b, c, d, e, f, pts_x, pts_y):
  y = (c*d - a*f) / (b*d - a*e)
  x = (f - e*y) / d
  pts_x.append(x)
  pts_y.append(y)

pts_x = []
pts_y = []

intersection(5, 4, 200, 3, 5, 150, pts_x, pts_y) #green and red
intersection(1, 0, 0, 3, 5, 150, pts_x, pts_y) #red and orange
intersection(1, 0, 0, 5, 4, 100, pts_x, pts_y) #purple and orange
intersection(0, 1, 0, 5, 4, 100, pts_x, pts_y) #purple and blue
intersection(0, 1, 0, 5, 4, 200, pts_x, pts_y) #green and blue

plt.plot(x, y5, label='y >= 0')
plt.plot(y5, x, label='x >= 0')
plt.plot(x, y1, label='5x + 4y <= 200')
plt.plot(x, y2, label='3x + 5y <= 150')
plt.plot(x, y3, label='5x + 4y >= 100')
plt.plot(x, y4, label='8x + 4y >= 80')
plt.xlabel('coordinates')
plt.ylabel('abcissa')
plt.legend()
plt.xlim(-1, 51)
plt.ylim(-1, 51)


up = np.minimum(y1, y2)
lo = np.maximum(y3, y4)
lo = np.maximum(lo, y5)
plt.fill_between(x, up, lo, where= up>lo, color='grey', alpha=0.5)
plt.scatter(pts_x, pts_y, color='black')

plt.show()

