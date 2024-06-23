import numpy as np

def activation(v):
    return 1 if v <= 0.5 else 0

def perceptron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NOT(x):
    w = np.array([1])
    b = 0.5
    return perceptron(x, w, b)

print(NOT(np.array([0])))
print(NOT(np.array([1])))
