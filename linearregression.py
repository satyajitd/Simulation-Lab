import numpy as np
import matplotlib.pyplot as plt

# Creation of dataset

x = np.random.normal(loc=0, scale=10, size=100)
y = 15 * x + 5 + np.random.normal(loc=0, scale=10, size=100)

plt.scatter(x, y)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.xlim(-7.5, 7.5)
plt.ylim(-100, 100)

plt.show()

def estimate_coef(x, y): 
  
  # number of observations/points 
  n = np.size(x) 

  # mean of x and y vector 
  m_x, m_y = np.mean(x), np.mean(y) 

  # calculating regression coefficients 
  b_1 = np.sum((x - m_x)*(y - m_y)) / np.sum((x - m_x)**2) 
  b_0 = m_y - b_1*m_x 

  return(b_0, b_1)

def plot_regression_line(x, y, b): 
    
  plt.scatter(x, y)

  # predicted response vector 
  y_pred = b[0] + b[1]*x 

  # plotting the regression line 
  plt.plot(x, y_pred, color = "g", linestyle = '-', linewidth = 1) 

  # putting labels 
  plt.xlabel('x-axis') 
  plt.ylabel('y-axis')

  plt.xlim(-7.5, 7.5)
  plt.ylim(-100, 100)

  # function to show plot 
  plt.show() 
  return y_pred

y_pred = plot_regression_line(x, y, estimate_coef(x, y))

SS_res = np.sum((y - y_pred)**2)
SS_total = np.sum((y - np.mean(y))**2)

R2 = 1 - SS_res / SS_total

print("R-squared: ", R2)

n = np.size(x)
rho = (n * (np.sum(x * y) - np.sum(x)) * np.sum(y)) / (np.sqrt((n * np.sum(x**2) - np.sum(x)**2)*(n * np.sum(y**2) - np.sum(y)**2)))

print("Rho: ", rho)