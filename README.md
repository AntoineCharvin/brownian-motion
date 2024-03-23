 # brownian-motion
# 3D Brownian Motion Simulation with Pygame and OpenGL

This Python application simulates and visualizes the Brownian motion of particles in a 3D space using Pygame and OpenGL. The Brownian motion is a random motion of particles suspended in a fluid (liquid or gas), as they collide with other fast-moving molecules in the fluid.

## Features

- Simulates 3D Brownian motion of 500 particles.
- Visualizes the particle trajectories in real-time using OpenGL.
- Allows users to view the simulation from different angles by rotating the scene.

## Prerequisites

Before running this application, you will need Python installed on your system along with the Pygame, OpenGL, and NumPy libraries.

## Installation

1. Ensure Python is installed on your system.
2. Install the required libraries using pip:

```bash
pip install pygame PyOpenGL numpy
```
## How to Use
- Once the simulation starts, it will automatically progress through the time steps, visualizing the particles' movement in 3D.
- The simulation window will display the particles moving in real-time.
- The simulation can be exited at any time by closing the Pygame window.

## Simulation Details
- The simulation initializes 500 particles with random initial positions.
- Each particle undergoes Brownian motion, simulated over 10,000 time steps.
- The simulation uses a simple Euler-Maruyama method to update particle positions based on their drift and volatility.
