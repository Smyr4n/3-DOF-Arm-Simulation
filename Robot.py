import numpy as np

import Utility

class Robot():
    
    def __init__(self):
        """
        Creates the Robot to simulate.
        """

        d = np.array([0, 0, 0])
        theta = np.array([0, 0, 0])
        a = np.array([0, 2, 2])
        alpha = np.array([np.pi/2, 0, 0])

        frames = 3
        zero_config = np.eye(4)

        for i in range(frames):
            pass

    def FK(self, joint1, joint2, joint3):
        """
        Returns the Homogeneous Transformation of the current pose.
        """

    def IK(self):
        """
        Returns the joint space coordinates of the desired pose.
        """