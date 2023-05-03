import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from yahoo_fin import stock_info as si
from collections import deque

import os
import numpy as np
import pandas as pd
import random

from data_preparation import load_data
from model_creation import create_model

def make_paths():
    if not os.path.isdir("results"):
        os.mkdir("results")
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    if not os.path.isdir("data"):
        os.mkdir("data")

def main():

    # gpus = tf.config.list_physical_devices('GPU')
    # if gpus:
    # # Restrict TensorFlow to only use the first GPU
    #     try:
    #         tf.config.set_visible_devices(gpus[0], 'GPU')
    #         tf.config.experimental.set_memory_growth(gpus[0], enable=True)
    #         logical_gpus = tf.config.list_logical_devices('GPU')
    #         print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
    #     except RuntimeError as e:
    #         # Visible devices must be set before GPUs have been initialized
    #         print(e)



    data = load_data("./datasets/hg=f.csv", 20, shuffle=True)
    model = create_model(20, 5, 16, 256)
    model_name = "test3"
    make_paths()

    checkpointer = ModelCheckpoint(os.path.join("results", model_name + ".h5"), save_best_only=True, verbose=1)
    tensorboard = TensorBoard(log_dir=os.path.join("logs", model_name))
    history = model.fit(data["X_train"], data["Y_train"],
                    batch_size=64,
                    epochs=50,
                    validation_data=(data["X_test"], data["Y_test"]),
                    callbacks=[checkpointer, tensorboard],
                    verbose=1)
    
if __name__ == "__main__":
    main()
