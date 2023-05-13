import json
import os
import tensorflow as tf

import json
import numpy as np

image_width = 160
image_height = 160
image_color_channel = 3
image_color_channel_size = 255
image_size = (image_width, image_height)
image_shape = image_size + (image_color_channel,)

batch_size = 32
epochs = 20
learning_rate = 0.0001

model = tf.keras.models.load_model('model')


def json_serializable(obj):
    if isinstance(obj, np.float32):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def teste(x):
    
    image = tf.keras.preprocessing.image.load_img(x, target_size=image_size)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)

    prediction = model.predict(image)[0][0]

    result = {'prediction': prediction, 'class': 'cat' if prediction < 0.5 else 'dog'}

    return json.dumps(result, default=json_serializable)

