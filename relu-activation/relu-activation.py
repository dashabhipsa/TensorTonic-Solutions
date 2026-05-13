import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.asarray(x, dtype=float)
    y = 0
    y = np.asarray(y, dtype=float)
    return np.maximum(y,x)
    pass