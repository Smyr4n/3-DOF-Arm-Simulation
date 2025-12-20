import numpy as np
import numpy.typing as npt

def SSM(K: npt.NDArray):
    """
    Converts the given 3x1 vector into a skew-symmetric matrix.

    Parameters:
        K (Numpy Array): 3x1 vector to transform

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