# Multivariate Constrained Optimization Technique
from sympy import symbols, diff, Eq, solve
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

x1, x2, l1, l2, s1, s2 = symbols('x1, x2, l1, l2, s1, s2', real=True)

f = (10*x1 - x1**2 + 10*x2 - x2**2) - l1*(x1 + x2 + s1**2 - 14) - l2*(-x1 + x2 + s2**2 - 6)

print("Lagrange's function: ", f)

dfdx1 = diff(f, x1)
dfdx2 = diff(f, x2)
dfds1 = diff(f, s1)
dfds2 = diff(f, s2)
dfdl1 = diff(f, l1)
dfdl2 = diff(f, l2)

print("\nPartial diff. of 'f' wrt 'x1': ", dfdx1)
print("Partial diff. of 'f' wrt 'x2': ", dfdx2)
print("Partial diff. of 'f' wrt 's1': ", dfds1)
print("Partial diff. of 'f' wrt 's2': ", dfds2)
print("Partial diff. of 'f' wrt 'l1': ", dfdl1)
print("Partial diff. of 'f' wrt 'l2': ", dfdl2)

eq1 = Eq(dfdx1)
eq2 = Eq(dfdx2)
eq3 = Eq(dfdl1)
eq4 = Eq(dfdl2)
eq5 = Eq(dfds1)
eq6 = Eq(dfds2)

sol = solve((eq1, eq2, eq3, eq4, eq5, eq6), (x1, x2, l1, l2, s1, s2))

ANS = []
x_a = []
y_a = []
for x_1, x_2, l_1, l_2, s_1, s_2 in sol:
    #print(x_1, x_2, l_1, l_2, s_1, s_2)
    if((l_1 == 0 and l_2 == 0) or (s_1 == 0 and s_2 == 0)):
        x_a.append(x_1)
        y_a.append(x_2)
        ANS.append((x_1, x_2, l_1, l_2, s_1, s_2))

dfdx1x1 = diff(dfdx1, x1)
dfdx1x2 = diff(dfdx1, x2)
dfdx2x2 = diff(dfdx2, x2)
dfdx2x1 = diff(dfdx2, x1)

print("\nPartial diff. of 'df/dx_1' wrt 'x1': ", dfdx1x1)
print("Partial diff. of 'df/dx_1' wrt 'x2': ", dfdx1x2)
print("Partial diff. of 'df/dx_2' wrt 'x1': ", dfdx2x1)
print("Partial diff. of 'df/dx_2' wrt 'x2': ", dfdx2x2)

m1 = dfdx1x1
m2 = dfdx1x1 * dfdx2x2 - dfdx1x2 * dfdx2x1 

print("\n")
for ans in ANS:
    if m1 > 0 and m2 > 0:
        print("Local minima at ", ans[0], ans[1])
        print(ans[0]*10 - ans[0]**2 + 10*ans[1] - ans[1]**2)
   
    elif m1 < 0 and m2 > 0:
        print("Local maxima at ", ans[0], ans[1])
        print(ans[0]*10 - ans[0]**2 + 10*ans[1]- ans[1]**2)
    
    else:
        print("Saddle point")


# plotting
x = np.linspace(-10, 50, 100)
y = np.linspace(-10, 50, 100)
X, Y = np.meshgrid(x, y)
Z = 10 * X - X ** 2 + 10 * Y - Y ** 2
plt.scatter(x_a, y_a, color="blue")
plt.contour(X, Y, Z, colors='red')
plt.show()