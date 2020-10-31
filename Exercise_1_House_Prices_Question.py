import tensorflow as tf
import numpy as np
from tensorflow import keras

# GRADED FUNCTION: house_model
def house_model(y_new):
    xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([50,100,150,200,250], dtype=float)

    model = tf.keras.Sequential([keras.layers.Dense(units=12, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs,ys,epochs=1000)
    return model.predict(y_new)[0]
def main():
    print('hi')
    prediction = house_model([7.0])
    print(prediction)
if __name__ == '__main__':
    main()