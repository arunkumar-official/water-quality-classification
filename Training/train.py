import tensorflow as tf
import pickle

from tensorflow import keras

train = keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255)
test = keras.preprocessing.image.ImageDataGenerator(rescale=1 / 255)

train_dataset = train.flow_from_directory("image_classify/",
                                          target_size=(200, 200), batch_size=3, class_mode="binary")
test_dataset = train.flow_from_directory("test/",
                                         target_size=(200, 200), batch_size=3, class_mode="binary")

model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
                                    tf.keras.layers.MaxPool2D(2, 2),
                                    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPool2D(2, 2),
                                    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                    tf.keras.layers.MaxPool2D(2, 2),
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(512, activation='relu'),
                                    tf.keras.layers.Dense(1, activation='sigmoid')

                                    ])

model.compile(loss='binary_crossentropy',
              optimizer=keras.optimizers.RMSprop(lr=0.001),
              metrics=['accuracy'])

model_fit = model.fit(train_dataset,
                      steps_per_epoch=5,
                      epochs=30,
                      validation_data=test_dataset)


pickle.dump(model, open("../model/water_modl_lcl.pkl", "wb"))
