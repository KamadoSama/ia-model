import os
import sys
import tensorflow as tf
print(f"Python version: {sys.version}")
print(f"TensorFlow version: {tf.__version__}")
try:
    print(f"Physical devices: {tf.config.list_physical_devices()}")
except Exception as e:
    print(f"Error listing devices: {e}")

# Try a small model to see if it crashes
model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
model.compile(optimizer='adam', loss='mse')
print("Model created and compiled successfully.")
