# 3-DOF Arm Simulation Project 🦾

## Overview 📰
This project is a Python-exclusive simulation that calculates the forward kinematics of a robot using DH Parameters and visualizes them using Matplotlib. 

The zero configuration parameters of the robot can be adjusted in the Config.json file. The robot only uses rotary joints and no prismatic joints.

## Review ✏️

This project was a simple test I wanted to give myself to see how well I could apply some of the knowledge I've learned from my Robotics courses. Due to the small scope and the simplicity of the project, Python was used, thanks to its variety of libraries (Numpy, Matplotlib, etc.).

Due to the use of Python, visualization is rather constrained, requiring specific Matplotlib techniques. I had opted for a dynamic plot that rescales itself to keep the robot in focus, but an alternative method would be to calculate the robot workspace prematurely and use it to create a static plot. While my approach is slightly more complicated, I think it does a better job helping to visualize how the simulated robot moves.

Overall this was a really interesting project to work on, and it helped me get used to fundamentals of programming robots in an environment that isn't ROS or RViz.
