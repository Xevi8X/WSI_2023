import tensorflow as tf
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from yahoo_fin import stock_info as si
from collections import deque

import os
import numpy as np
import pandas as pd
import random

def load_data(dataFileName, historyLength, lookupStep=1, testSize=0.2, shuffle=False, scale=True):
    result = dict()
    features = ['Date', 'Open', 'High', 'Close', 'Low', 'Volume']

    df = pd.read_csv(dataFileName)
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
    # df['Future'] = df['Close'] / df['Future']
    # print(df['Future'])
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

    X = np.array(X)
    Y = np.array(Y)

    result["X_train"], result["X_test"], result["Y_train"], result["Y_test"] = train_test_split(X, Y, test_size=testSize, shuffle=shuffle)
    result["X_train"] = result["X_train"][:, :, 1:].astype(np.float32)
    result["X_test"] = result["X_test"][:, :, 1:].astype(np.float32)
    
    return result
