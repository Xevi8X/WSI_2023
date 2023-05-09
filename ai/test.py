import numpy as np
import pandas as pd
import tensorflow as tf
from collections import deque
from sklearn import preprocessing
import matplotlib.pyplot as plt

from model_creation import create_model

def plot_graph(test_df):
    """
    This function plots true close price along with predicted close price
    with blue and red colors respectively
    """
    # temp = []
    # for i in range(len(test_df['Y_test'])):
    #     temp.append(abs(test_df['Y_pred'][i][0] - test_df['Y_test'][i]))
    
    # plt.subplot(1, 2, 1)
    # plt.plot(test_df['Y_test'][:-1], c='b')
    # plt.plot(test_df['Y_pred'][1:], c='r')
    plt.plot(test_df['Y_test'], c='b')
    plt.plot(test_df['Y_pred'], c='r')
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend(["Actual Price", "Predicted Price"])

    # plt.subplot(1, 2, 2)
    # plt.plot(temp, c='b')
    # plt.xlabel("Days")
    # plt.ylabel("Absolute Error")
    plt.show()


def prepare_test_data(path, historyLength, lookupStep=1, scale=True):
    result = dict()
    features = ['Date', 'Open', 'High', 'Close', 'Low', 'Volume']
    df = pd.read_csv(path)
    result['df'] = df.copy()
    
    if scale:
        column_scaler = {}
        # scale the data (prices) from 0 to 1
        for column in features:
            if column == 'Date':
                continue
            scaler = preprocessing.MinMaxScaler()
            df[column] = scaler.fit_transform(np.expand_dims(df[column].values, axis=1))
            column_scaler[column] = scaler
        # add the MinMaxScaler instances to the result returned
        result["column_scaler"] = column_scaler

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
    data = prepare_test_data("./datasets/hg=f.csv", 20, 1, 5)
    model = tf.keras.models.load_model('./results/testGPU_XS_Long_LLR.h5')
    y_pred = model.predict(data['X_test'])

    y_test = np.squeeze(data["column_scaler"]["Close"].inverse_transform(np.expand_dims(data['Y_test'], axis=0)))
    y_pred = np.squeeze(data["column_scaler"]["Close"].inverse_transform(y_pred))

    data['Y_test'] = y_test
    data['Y_pred'] = y_pred
    plot_graph(data)
    print(model.summary())

if __name__ == "__main__":
    main()