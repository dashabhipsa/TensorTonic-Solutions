import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.asarray(x, dtype=float)
    y = []
    for i in x:
        if i>0:
            y.append(i)
        else:
            y.append(alpha*(np.exp(i)-1))
    return y        
    pass