import sys
import os
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard

from constants import *
from train import make_paths
from data_preparation import load_data


def train_single_stock(stock_path: str, epoch_number: int, batch_size: int, output_model_path: str):
    data = load_data(stock_path, NUMBER_OF_DAYS, shuffle=SHUFFLE, lookupStep = LOOKUP_STEP)

    model = tf.keras.models.load_model(FINAL_MODEL)
    make_paths()
    checkpointer = ModelCheckpoint(output_model_path, save_best_only=True, verbose=1)
    tensorboard = TensorBoard(log_dir=os.path.join("logs", MODEL_NAME))
    history = model.fit(data["X_train"], data["Y_train"],
                    batch_size=batch_size,
                    epochs=epoch_number,
                    validation_data=(data["X_test"], data["Y_test"]),
                    callbacks=[checkpointer, tensorboard],
                    verbose=1)

if __name__ == "__main__":
    if len(sys.argv) == 5:
        train_single_stock(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    else:
        print("Expected input:")
        print("1) Path to stock CSV")
        print("2) Number of epochs")
        print("3) Batch size")
        print("4) Path for model to be saved")
