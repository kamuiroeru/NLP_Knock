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


from random import sample


def train(fi, n=30) -> dict:
    t = 1
    W = collections.defaultdict(float)
    # Loop for instances.
    for n in range(n):
        for line in sample(fi, len(fi)):
            fields = line.strip('\n').split(' ')
            update(W, fields[1:], float(1 if fields[0] == '+1' else 0), eta0 / (1 + t / float(N)))
            t += 1
    return W

if __name__ == '__main__':
    from k72 import remove_waste
    import pickle
    inputList = []
    for line in open('sentiment.txt'):
        lineSplit = line.rstrip().split(' ')
        inputList.append(' '.join([lineSplit[0]] + remove_waste(lineSplit[1:])))

    pickle.dump(train(inputList), open('model.pkl', 'wb'))
    print('Complete!')
