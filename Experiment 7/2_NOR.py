import numpy as np

def activation(v):
    return 1 if v <= 0.5 else 0

def perceptron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NOR(x):
    w = np.array([1, 1])
    b = 0.5
    return perceptron(x, w, b)

print(NOR(np.array([0, 0])))
print(NOR(np.array([0, 1])))
print(NOR(np.array([1, 0])))
print(NOR(np.array([1, 1])))