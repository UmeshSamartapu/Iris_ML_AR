import numpy as np

def preprocess(data):
    return np.array(data).reshape(1, -1)