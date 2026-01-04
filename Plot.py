import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
from mpl_toolkits.mplot3d import Axes3D

import Robot
import Utility

robot = Robot.Robot()
fig = plt.figure(figsize=(8, 8))
ax3D = fig.add_subplot(111, projection='3d')

def _Plot_Arm(ax, Ts):
    ax.cla()

    pos = []
    for T in Ts:
        pos.append(T[:3, 3])
    pos = np.array(pos)

    ax.plot(pos[:, 0], pos[:, 1], pos[:, 2], marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])

    max_range = np.max(np.ptp(pos, axis=0)) + 0.5
    mid = np.mean(pos, axis=0)
    ax.set_xlim(mid[0]-max_range/2, mid[0]+max_range/2)
    ax.set_ylim(mid[1]-max_range/2, mid[1]+max_range/2)
    ax.set_zlim(mid[2]-max_range/2, mid[2]+max_range/2)
    plt.draw()

slider_pos = [
    [0.15, 0.03, 0.7, 0.03],
    [0.15, 0.07, 0.7, 0.03],
    [0.15, 0.11, 0.7, 0.03]
]

theta1_slider = Slider(plt.axes((0.15, 0.10, 0.7, 0.03)), 'θ1: ', -180.0, 180.0, valinit=0.0)
theta2_slider = Slider(plt.axes((0.15, 0.15, 0.7, 0.03)), 'θ2: ', -180.0, 180.0, valinit=0.0)
theta3_slider = Slider(plt.axes((0.15, 0.20, 0.7, 0.03)), 'θ3: ', -180.0, 180.0, valinit=0.0)

def _Update(event=None):
    thetas = np.array([theta1_slider.val, theta2_slider.val, theta3_slider.val])
    thetas = np.deg2rad(thetas)
    Ts = robot.FK(thetas)
    _Plot_Arm(ax3D, Ts)
    fig.canvas.draw_idle()

theta1_slider.on_changed(_Update)
theta2_slider.on_changed(_Update)
theta3_slider.on_changed(_Update)

plt.title("3-DOF Robot Arm Simulation")
plt.show()