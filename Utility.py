import numpy as np
import numpy.typing as npt
from scipy.linalg import expm

def SSM(K: npt.NDArray):
    """
    Converts the given 1x3 vector into a skew-symmetric matrix.

    Parameters:
        K (Numpy Array): 1x3 vector to transform

    Returns:
        S (Numpy Array): 3x3 skew-symmetric matrix of the given vector.
    """
    
    ssm = np.array([
        [0, -K[2] , K[1]],
        [K[2], 0, -K[0]],
        [-K[1], K[0], 0]
    ])

    return ssm

def Translate(D: npt.NDArray) -> npt.NDArray:
    """
    Returns a transformation matrix with the given 1x3 displacement vector.
    """
    T = np.array([
        [1, 0, 0, D[0]],
        [0, 1, 0, D[1]],
        [0, 0, 1, D[2]],
        [0, 0, 0, 1]
    ])

    return T

def Rotate(KTheta: npt.NDArray) -> npt.NDArray:
    """
    Returns a transformation matrix rotating about the vector K * Theta.
    """
    ssm = SSM(KTheta)
    T = np.block([
        [expm(ssm), np.zeros((3, 1))],
        [np.zeros((1, 3)), 1]
    ])

    return T