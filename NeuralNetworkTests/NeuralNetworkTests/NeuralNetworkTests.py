"""
Landon Buell
11 Sept 2020
"""

        #### IMPORTS ####

import numpy as np
import os
import tensorflow as tf
import tensorflow.keras as keras

        #### EXECUTABLE ####

if __name__ == '__main__':

    myCNN = keras.models.Sequential(name="CNN")

    myCNN.add(keras.layers.InputLayer(input_shape=(32,32,3)))
    
    myCNN.add(keras.layers.Conv2D(filters=32,kernel_size=(3,3),strides=(1,1),activation='relu'))
    myCNN.add(keras.layers.Conv2D(filters=32,kernel_size=(3,3),strides=(1,1),activation='relu'))
    myCNN.add(keras.layers.Flatten())

    myCNN.add(keras.layers.Dense(units=64,activation='relu'))
    myCNN.add(keras.layers.Dense(units=64,activation='relu'))

    myCNN.compile(optimizer="Categorical_Crossentropy",
                  loss='SGD')

    print("=)")

