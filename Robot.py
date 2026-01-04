import numpy as np
import numpy.typing as npt

import Utility

class Robot():
    
    def __init__(self, d, a, alpha):
        """
        Creates the Robot to simulate.
        """

        # Zero Configuration Parameters
        self.d = np.array(d)
        self.a = np.array(a)
        self.alpha = np.array(alpha)

        if len(self.d) != len(self.a) != len(self.alpha) != 3:
            raise ValueError("Each config parameter must have 3 frames!")
        
        self.frames = 3

        # Create the Zero Configuration of the Robot
        self.zero_config = self.FK(np.zeros(3))
        

    def FK(self, theta: npt.NDArray):
        """
        Returns the Homogeneous Transformations of each frame.
        """
        Ts = []
        T = np.eye(4)
        for i in range(self.frames):
            T = T @ Utility.Rotate(np.array([0, 0, theta[i]]))
            T = T @ Utility.Translate(np.array([0, 0, self.d[i]]))
            T = T @ Utility.Translate(np.array([self.a[i], 0, 0]))
            T = T @ Utility.Rotate(np.array([self.alpha[i], 0, 0]))
            Ts.append(T.copy())
        return np.array(Ts)