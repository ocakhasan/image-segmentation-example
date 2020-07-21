import tensorflow as tf
import PIL
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from cv2 import imwrite, resize
import matplotlib.pyplot as plt
import os

global graph
graph = tf.compat.v1.get_default_graph()

def create_mask(pred_mask):
  pred_mask = tf.argmax(pred_mask, axis=-1)
  pred_mask = pred_mask[..., tf.newaxis]
  return pred_mask[0]

def get_prediction(model, filename):

    image_for_size = PIL.Image.open(filename)
    width, height = image_for_size.size

    print("Width and height is {}, {}".format(width, height))
    print("filename is, ", filename)
    
    filename_without_folder = filename.split('/')[2]
    filename_raw, file_extension = os.path.splitext(filename_without_folder)

    img = load_img(filename, target_size=(128, 128))
    array_img = img_to_array(img)
    array_img = array_img / 255.0
    image = array_img.reshape((1, array_img.shape[0], array_img.shape[1], array_img.shape[2]))
    prediction = model.predict(image)
    preds_shaped = prediction.reshape((128,128,3))
    mask_prediction = create_mask(prediction)
    image_from_array = array_to_img(mask_prediction)
    resized = resize(np.array(image_from_array), (width, height))

    url_for_image = filename_raw + "_mask_" + file_extension

    imwrite("static/" + url_for_image, resized)

    return url_for_image


