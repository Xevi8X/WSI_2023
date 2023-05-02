from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split

def create_model(nSequence, nFeatures, nLayers, units, dropout=0.3):
    model = Sequential()

    # First layer
    model.add(LSTM(units, return_sequences=True, batch_input_shape=(None, nSequence, nFeatures)))
    model.add(Dropout(dropout))
    
    for i in range(nLayers):
        model.add(LSTM(units, return_sequences=True))
        model.add(Dropout(dropout))

    # Last layer
    model.add(LSTM(units, return_sequences=False))
    model.add(Dropout(dropout))
    model.add(Dense(1, activation="linear"))

    model.compile(loss="mean_absolute_error", metrics=["mean_absolute_error"], optimizer="Adam")
    return model


# m = create_model(20, 5, 16, 256)
# m.build()
# print(m.summary())