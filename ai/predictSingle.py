import sys
import tensorflow as tf
import numpy as np

from ai.constants import *
from ai.test import prepare_test_data

def predict_single(stock_path: str, inputModelPath: str) -> list:
    data = prepare_test_data(stock_path, NUMBER_OF_DAYS, LOOKUP_STEP)
    model = tf.keras.models.load_model(inputModelPath)
    y_pred = model.predict(data['X_test'])
    y_pred = np.squeeze(data["column_scaler"]["Close"].inverse_transform(y_pred))
    return y_pred[-LOOKUP_STEP:]


def predict(stock_path: str, inputModelPath: str, numberOfDays: int) -> list:
    data = prepare_test_data(stock_path, NUMBER_OF_DAYS, LOOKUP_STEP)
    model = tf.keras.models.load_model(inputModelPath)
    y_pred = model.predict(data['X_test'])

    y_test = np.squeeze(data["column_scaler"]["Close"].inverse_transform(np.expand_dims(data['Y_test'], axis=0)))
    y_pred = np.squeeze(data["column_scaler"]["Close"].inverse_transform(y_pred))
    return y_test[-numberOfDays:], y_pred[-numberOfDays:]

if __name__ == "__main__":
    real, predict = predict(sys.argv[1], sys.argv[2], 30)
    for i, pred in enumerate(predict):
        print(f"For day in the future number {i + 1} predicted closing price is: {pred}, real price is {real[i]}")
