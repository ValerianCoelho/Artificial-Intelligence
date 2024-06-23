import numpy as np

def activation(v):
    return 0 if v <= 2.5 else 1

def perceptron(x, w, b):
    r = np.dot(x, w) + b
    return activation(r)

def AND(x):
    w = np.array([1, 1, 1])
    b = 0.5
    return perceptron(x, w, b)

print(AND(np.array([0, 0, 0])))
print(AND(np.array([0, 0, 1])))
print(AND(np.array([0, 1, 0])))
print(AND(np.array([0, 1, 1])))
print(AND(np.array([1, 0, 0])))
print(AND(np.array([1, 0, 1])))
print(AND(np.array([1, 1, 0])))
print(AND(np.array([1, 1, 1])))