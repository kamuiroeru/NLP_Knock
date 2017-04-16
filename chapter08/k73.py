import collections
import math

N = 10662  # Change this to present the number of training instances.
eta0 = 0.1  # Initial learning rate; change this if desired.


def sigmoid(x: float) -> float:
    return 1. / (1. + math.exp(-x))


def update(W, X, l, eta):
    # Compute the inner product of features and their weights.
    a = sum([W[x] for x in X])

    # Compute the gradient of the error function (avoiding +Inf overflow).
    g = (sigmoid(a) - l) if -100. < a else (0. - l)

    # Update the feature weights by Stochastic Gradient Descent.
    for x in X:
        W[x] -= eta * g


def train(fi):
    t = 1
    W = collections.defaultdict(float)
    # Loop for instances.
    for line in fi:
        fields = line.strip('\n').split(' ')
        update(W, fields[1:], float(fields[0]), eta0 / (1 + t / float(N)))
        t += 1
    return W
