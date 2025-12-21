import numpy as np
import numpy.typing as npt

def Translate(D: npt.NDArray):
    """
    Returns a transformation matrix with the given 1x3 displacement vector.
    """
    T = np.array([
        [0, 0, 0, D[0]],
        [0, 0, 0, D[1]],
        [0, 0, 0, D[2]],
        [0, 0, 0, 1]
    ])

    return T

def SSM(K: npt.NDArray):
    """
    Converts the given 1x3 vector into a skew-symmetric matrix.

    Parameters:
        K (Numpy Array): 1x3 vector to transform

    Returns:
        S (Numpy Array): 3x3 skew-symmetric matrix of the given vector.
    """
    if K.shape != (3, 1):
        return None
    
    ssm = np.array([
        [0, -K[3] , K[2]],
        [K[3], 0, -K[1]],
        [-K[2], K[1], 0]
    ])

    return ssm