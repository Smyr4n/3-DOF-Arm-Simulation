import numpy as np

class Robot():
    
    def __init__(self, link1, link2, link3):
        """
        Creates the Robot to simulate.
        Each joint in the robot is a rotary joint.
        Each link parameter determines the length of the corresponding link.

        Parameters:
            link1 (float): Length of Link 1
            link2 (float): Length of Link 2
            link3 (float): Length of Link 3
        """
        self.link1 = link1
        self.link2 = link2
        self.link3 = link3

        total_link_length = link1 + link2 + link3

        self.zeroconfig = np.array([
            [1, 0, 0, total_link_length],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def FK(self, joint1, joint2, joint3):
        """
        Returns the Homogeneous Transformation of the current pose.

        Parameters:
            joint1 (float): Degree of Joint 1
            joint2 (float): Degree of Joint 2
            joint3 (float): Degree of Joint 3
        """

    def IK(self):
        """
        Returns the joint space coordinates of the desired pose.
        """