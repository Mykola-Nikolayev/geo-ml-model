import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# paramet
img_size = 224      # img size can be smaller if needed
batch_size = 32     # size of the batch
num_classes = 3     # that for 3 class (3 form)
epochs = 10         # nomber of epochs

# repo of dataset
train_dir = 'dataset/train'
val_dir = 'dataset/validation'
test_dir = 'dataset/test'

# creation of data to train and validation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,

)