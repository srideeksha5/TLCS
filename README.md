##  Deep Q-Learning Based Traffic Signal Control System

An AI-powered Traffic Light Control System using **Deep Q-Learning (DQN)** to dynamically optimize signal timings and reduce traffic congestion in simulated urban intersections.


##  Problem Statement

Urban traffic congestion is a growing issue with fixed-time signal systems failing to adapt to dynamic conditions. This project introduces a reinforcement learning-based solution that adjusts traffic lights in real-time to improve flow and reduce delays.

## Objectives

- Train a DQN agent to optimize traffic signal phases.
- Simulate real-time traffic using SUMO (Simulation of Urban MObility).
- Minimize average queue length, delay, and congestion.
- Adapt to changing traffic patterns through learning.
- 
##  Features

- **State**: 80-dimensional binary vector representing vehicle presence on 8 lanes.
- **Actions**: 4 signal phases (NS, NSL, EW, EWL).
- **Rewards**: Based on reduction in total vehicle wait time.
- **Training**: Experience replay, epsilon-greedy policy, Bellman updates.
- **Visualization**: Graphs of performance metrics over training episodes.

## Technologies Used

- Python, Keras, TensorFlow
- SUMO (TraCI API)
- NumPy, Matplotlib

##  Results Summary

-  **Average Queue Length**: Reduced from ~14 to ~3-4 vehicles.
-  **Cumulative Delay**: Dropped from ~80,000s to ~15,000s.
-  **Negative Rewards**: Improved from -60,000 to -10,000, indicating learning convergence.

