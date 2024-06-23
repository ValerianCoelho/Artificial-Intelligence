import numpy as np

def activation(v):
    return 1 if v <= 1.5 else 0

def perceptron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def NAND(x):
    w = np.array([1, 1])
    b = 0.5
    return perceptron(x, w, b)

print(NAND(np.array([0, 0])))
print(NAND(np.array([0, 1])))
print(NAND(np.array([1, 0])))
print(NAND(np.array([1, 1])))