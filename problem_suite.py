import numpy as np

def func1(x):
    return np.sum(x)

def func2(x):
    return np.linalg.norm(x)

problems = {
    "func1" : func1,
    "func2" : func2,
    "func3" : func2
}

meta_dims = {
    "func1" : 5,
    "func2" : 5,
    "func3" : 15
}

