import tensorflow as tf 

# We get the dataset fashing mnist object
mnist = tf.keras.datasets.fashion_mnist

# We load the data set,
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# Sample to get the frist image
import numpy as np
np.set_printoptions(linewidth=200)
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

training_images  = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape = (28,28)), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

