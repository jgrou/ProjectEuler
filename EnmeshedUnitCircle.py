from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

N = 10
n = N//2

def A(t):
    res = 0
    t = np.append(0,t)
    if n&1:
        t = np.append(t, np.pi/4)
    else:
        half = n//2
        res += (np.cos(t[half]) - np.sin(t[half])) * np.cos(t[half])
    for i in range((n+1)//2):
        res += (np.sin(t[i+1]) - np.sin(t[i])) * np.cos(t[i])
        res += (np.cos(t[i]) - np.cos(t[i+1])) * np.sin(t[i+1])
    return 4*res

# Define the constraints
constraints = []
for i in range(n//2 - 1):
    constraints.append({'type': 'ineq', 'fun': lambda x, i=i: x[i+1] - x[i]})  # x[i+1] > x[i]
constraints.append({'type': 'ineq', 'fun': lambda x: x[0]})  # x[0] > 0
constraints.append({'type': 'ineq', 'fun': lambda x: np.pi/4 - x[-1]})  # y[-1] < pi/4

initial_guess = np.linspace(0, np.pi/4, n//2 + 2)[1:-1]
result = optimize.minimize(A, initial_guess, constraints=constraints)
ans = 0
while ans != result.fun:
    ans = result.fun
    result = optimize.minimize(A, result.x, constraints=constraints)
    
print(round(ans,10))

#%%
plt.figure(figsize=(10,10))
for x in np.sin(result.x):
    plt.plot([-1,1], (x,x), color='k')
    plt.plot([-1,1], (-x,-x), color='k')
    plt.plot((x,x), [-1,1], color='k')
    plt.plot((-x,-x), [-1,1], color='k')
    
for x in np.cos(result.x):
    plt.plot([-1,1], (x,x), color='k')
    plt.plot([-1,1], (-x,-x), color='k')
    plt.plot((x,x), [-1,1], color='k')
    plt.plot((-x,-x), [-1,1], color='k')
    
if n&1:
    for x in [0.5**0.5]:
        plt.plot([-1,1], (x,x), color='k')
        plt.plot([-1,1], (-x,-x), color='k')
        plt.plot((x,x), [-1,1], color='k')
        plt.plot((-x,-x), [-1,1], color='k')
    
plt.xlim(-1,1)
plt.ylim(-1,1)

t = np.linspace(0,np.pi*2)
plt.plot(np.cos(t), np.sin(t))