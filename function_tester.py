import numpy as np
import matplotlib.pyplot as plt
import money_functions as mf

def main():
    x = np.arange(-2, 2, 0.01)
    yS = np.vectorize(mf.sigmoid)(x)
    yT = np.vectorize(mf.tanh)(x)
    yO = np.vectorize(mf.optimal)(x)
    yB = np.vectorize(mf.randomBinary)(x)
    plt.plot(x, yS, c='r')
    plt.plot(x, yT, c='b')
    plt.plot(x, yO, c='g')
    plt.plot(x, yB, c='y')
    plt.legend(["Sigmoid", "Tanh", "Optimal", "Binary"])
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")
    plt.show()

if __name__ == "__main__":
    main()