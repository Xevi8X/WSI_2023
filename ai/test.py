import numpy as np
import pandas as pd
import tensorflow as tf
from collections import deque
import matplotlib.pyplot as plt

from model_creation import create_model

def plot_graph(test_df):
    """
    This function plots true close price along with predicted close price
    with blue and red colors respectively
    """
    temp = []
    for i in range(len(test_df['Y_test'])):
        temp.append(abs(test_df['Y_pred'][i][0] - test_df['Y_test'][i]))
    
    plt.subplot(1, 2, 1)
    plt.plot(test_df['Y_test'], c='b')
    plt.plot(test_df['Y_pred'], c='r')
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend(["Actual Price", "Predicted Price"])

    plt.subplot(1, 2, 2)
    plt.plot(temp, c='b')
    plt.xlabel("Days")
    plt.ylabel("Absolute Error")
    plt.show()


def prepare_test_data(path, historyLength, lookupStep=1):
    result = dict()
    features = ['Date', 'Open', 'High', 'Close', 'Low', 'Volume']
    df = pd.read_csv(path)
    result['df'] = df.copy()
    
    df['Future'] = df['Close'].shift(-lookupStep)
    df.dropna(inplace=True)

    sequence_data = []
    sequences = deque(maxlen=historyLength)
    for entry, target in zip(df[features].values, df['Future'].values):
        sequences.append(entry)
        if len(sequences) == historyLength:
            sequence_data.append([np.array(sequences), target])

    X, Y = [], []
    for seq, target in sequence_data:
        X.append(seq)
        Y.append(target)
    result['X_test'] = np.array(X)
    result['Y_test'] = np.array(Y)
    result["X_test"] = result["X_test"][:, :, 1:].astype(np.float32)
    return result

def main():
    data = prepare_test_data("./datasets/hg=f.csv", 20, 1)
    model = create_model(20, 5, 16, 256)
    model.load_weights('./results/test3.h5')
    y_pred = model.predict(data['X_test'])
    data['Y_pred'] = y_pred
    plot_graph(data)

if __name__ == "__main__":
    main()