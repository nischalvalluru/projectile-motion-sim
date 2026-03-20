# Projectile Motion Simulator
A numerical physics engine designed to simulate and visualise the trajectory of a projectile subject to gravitational force and non-linear atmospheric drag. This simulator utilises the **Euler-Cromer** integration method to maintain superior stability and physical accuracy.

## Physics Model

The simulator models the motion of a point-mass by solving coupled ordinary differential equations (ODEs). It accounts for two primary physical influences:

1. **Gravitational Acceleration:** A constant downward acceleration of $g = 9.81 \text{m/s}^2$.
2. **Quadratic Drag:** Air resistance is modelled as being proportional to the square of the instantaneous velocity. This is the standard model for projectiles where the force of air resistance becomes significantly more dominant at higher speeds: F = kv²

### Numerical Integration
Unlike the standard Euler method, this script employs the **Euler-Cromer** algorithm. By updating the velocity states before calculating the position states, the simulation preserves the symplectic nature of the system, leading to more reliable energy conservation over the flight duration.

## Features

* **Vectorised Calculations:** Leverages **NumPy** for efficient computation of velocity magnitudes and trigonometric transformations.
* **Technical Visualisation:** Generates high-resolution plots using **Matplotlib**, including automated axis scaling and physical units.
* **Configurable Parameters:** Initial conditions such as mass ($m$), drag coefficient ($k$), and launch velocity ($v_0$) are easily adjustable within the source code.


## Prerequisites

Ensure you have Python 3.x installed along with the following dependencies:

* **NumPy**
* **Matplotlib**

You can install these libraries using:

pip install numpy matplotlib

## How to Run
1. Clone the repository:
   `git clone https://github.com/nischalvalluru/projectile-motion-sim.git`
2. Run the script:
   `python main.py`

## License
This project is licensed under the MIT License.