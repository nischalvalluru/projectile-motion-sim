import numpy as np
import matplotlib.pyplot as plt

# Constants + initial conditions

v0 = 20
theta_degrees = 60
theta_rad = np.deg2rad(theta_degrees)
k = 0.1
m = 10
g = 9.81
dt = 0.001

vx, vy = v0 * np.cos(theta_rad), v0 * np.sin(theta_rad)
x, y = 0, 1e-9

x_vals = []
y_vals = []

while y > 0:
    v_mag = np.sqrt((vx)**2 + (vy)**2)

    ax = (-k/m) * v_mag * vx
    ay = -g + (-k/m) * v_mag * vy

    vx += (ax * dt)
    vy += (ay * dt)

    x += (vx * dt)
    y += (vy * dt)
    
    x_vals.append(x)
    y_vals.append(y)

plt.plot(x_vals, y_vals)
plt.xlabel("Distance / m")
plt.ylabel("Distance / m")
plt.title("Plot of projectile motion with air resistance")
plt.show()