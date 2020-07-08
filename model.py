import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import time
import loader
import matplotlib.pyplot as plt

EPOCHS = 100
TIME_STEP = 5


class Model:
    def __init__(self):
        #self.model = self.load()
        #self.build()
        self.model = self.load()

    def build(self):

        model = tf.keras.models.Sequential(
            [
                tf.keras.layers.LSTM(200, input_shape=(TIME_STEP, 400), return_sequences=True),
                tf.keras.layers.Dropout(0.2),

                tf.keras.layers.LSTM(200, input_shape=(TIME_STEP, 400)),
                tf.keras.layers.Dropout(0.2),

                tf.keras.layers.Dense(200, activation=tf.nn.relu),
                tf.keras.layers.Dropout(0.2),

                tf.keras.layers.Dense(10, activation=tf.nn.sigmoid)
            ]
        )

        model.compile(optimizer='adam', loss=tf.keras.losses.binary_crossentropy, metrics=['accuracy'])

        self.model = model

    def train(self):

        x_train, y_train = loader.load()
        x_train = x_train / 255

        top_5_percent = int(x_train.shape[0] * (5 / 100))
        x_val = x_train[:top_5_percent]
        y_val = y_train[:top_5_percent]

        history = self.model.fit(x_train, y_train, batch_size=32, epochs=EPOCHS, validation_data=(x_val, y_val))

        self.model.save("Test model 1")

        loss_train = history.history['loss']
        loss_val = history.history['val_loss']

        epochs = range(1, EPOCHS + 1)

        plt.plot(epochs, loss_train, 'g', label='Training loss')
        plt.plot(epochs, loss_val, 'b', label='Validation loss')

        plt.title("Loss")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.legend()
        plt.savefig('fig-loss.png')

        plt.clf()

        acc_train = history.history['accuracy']
        acc_val = history.history['val_accuracy']

        plt.plot(epochs, acc_train, 'g', label='Training Accuracy')
        plt.plot(epochs, acc_val, 'b', label='Validation Accuracy')

        plt.title("Accuracy")
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy")
        plt.legend()
        plt.savefig('fig-acc.png')

    def load(self):
        return tf.keras.models.load_model("Test model 1")

    def predict(self, image_stream):
        pred = self.model.predict(image_stream).flatten()
        out = []

        for i in pred:
            if i >= 0.7:
                out.append(1)
            else:
                out.append(0)

        return np.array(out)

    def summary(self):
        return self.model.summary()


if __name__ == '__main__':
    m = Model()
    m.build()
    m.train()
