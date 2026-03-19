# take values of: initial velocity (v), angle (theta), drag coefficient (k), time step (dt), mass (m)
# plot x and y positions on graph with matplotlib
# Fd = kv^2, F = ma => ad = kv^2/m. 
# ax = (-k/m)(√vx^2 + vy^2)(vx)
# ay = - g + (-k/m)(√vx^2 + vy^2)(vy)
# vx = v costheta
# vy = v sintheta 
# -------------------------------------
# Euler - Cromer method:
# x = x + ((vx + (ax * dt)) * dt)
# y = y + ((vy + (ay * dt)) * dt)
# While loop - while y > 0, compute x,y. 
# if y = 0, break. 
# x_values = []
# y_value = []
# for each time step, append x/y to x/y_values. 

import numpy as np
import matplotlib.pyplot as plt

v = 20
theta_degrees = 60
theta = np.deg2rad(theta_degrees)
k = 0.1
m = 5
g = 9.81
dt = 0.0001

vx = v * np.cos(theta)
vy = v * np.sin(theta)
ax = (-k/m) * (np.sqrt((vx)**2 + (vy)**2)) * vx
ay = - g + ((-k/m) * (np.sqrt((vx)**2 + (vy)**2)) * vy)

x_values = []
y_values = []
x = 0
y = 0.00000001

while y > 0:
    v_mag = np.sqrt((vx)**2 + (vy)**2)
    ax = (-k/m) * v_mag * vx
    vx += (ax * dt)
    x += (vx * dt)
    x_values.append(x)
    ay = -g + (-k/m) * v_mag * vy
    vy += (ay * dt)
    y += (vy * dt)
    y_values.append(y)

plt.plot(x_values, y_values)
plt.xlabel("Distance / m")
plt.ylabel("Distance / m")
plt.title("Plot of projectile motion with air resistance")
plt.show()
    