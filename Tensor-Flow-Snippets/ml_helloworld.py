import tensorflow as tf 
import numpy as np
from tensorflow import keras

# Testing neural network
# y = 2x - 1

# Neural network layers are created using Sequential function.
# In this case we create one layer only
# Create a neural network layer using Dense function, we only have one neuron
# We have flat input , just a set of number so units = 1, and shape is also linear so it is 1.

model = tf.keras.Sequential([keras.layers.Dense(1), keras.layers.Dense(1)])
model.compile(optimizer = "sgd", loss = "mean_squared_error")

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

model.fit(xs, ys, epochs = 500)
print("Model finished training.")

test_numbers = [10, 11, 12, 13, 14]

for num in test_numbers:    
    print("Prediction for x={}, y={}.".format(num, model.predict([num])))