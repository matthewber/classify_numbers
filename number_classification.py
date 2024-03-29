import tensorflow as tf

def make_datasets():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    print(x_test.shape)
    return (x_train, y_train), (x_test, y_test)


def make_and_eval_model():
    (x_train, y_train), (x_test, y_test) = make_datasets()
    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)), tf.keras.layers.Dense(128, activation='relu'), tf.keras.layers.Dropout(0.2), tf.keras.layers.Dense(10, activation='softmax')])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)
    return model

if __name__ == "__main__":
    make_datasets()

    #make_and_eval_model()
