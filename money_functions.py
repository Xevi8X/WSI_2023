import math
import random

def tanh(x):
    return math.tanh(10 * x)

def sigmoid(x):
    return 2 / (1 + math.exp(-5*x)) - 1

def optimal(x):
    minimal = 0.2
    if x < 0:
        minimal *= -1
    return math.tanh(3 * x + minimal)

def binary(x):
    return 1 if x > 0 else -1

def randomBinary(x):
    return (1 if x > 0 else -1) * random.uniform(0, 1)
