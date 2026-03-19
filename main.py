# take values of: initial velocity (v), angle (theta), drag coefficient (k), time step (dt)
# plot x and y positions on graph with matplotlib
# Fd = kv^2, F = ma => ad = kv^2/m. 
# ax = (-k/m)(√vx^2 + vy^2)(vx)
# ay = - g - (-k/m)(√vx^2 + vy^2)(vy)
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

