import numpy as np

def activation(v):
    return 1 if v <= 0.5 else 0

def perceptron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def OR(x):
    w = np.array([1, 1, 1])
    b = 0.5
    return perceptron(x, w, b)

print(OR(np.array([0, 0, 0])))
print(OR(np.array([0, 0, 1])))
print(OR(np.array([0, 1, 0])))
print(OR(np.array([0, 1, 1])))
print(OR(np.array([1, 0, 0])))
print(OR(np.array([1, 0, 1])))
print(OR(np.array([1, 1, 0])))
print(OR(np.array([1, 1, 1])))