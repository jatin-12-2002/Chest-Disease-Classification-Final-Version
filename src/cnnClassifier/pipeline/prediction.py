import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("model", "model.h5"))

        # Load image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Predict
        result = np.argmax(model.predict(test_image), axis=1)

        if result[0] == 0:
            prediction = 'adenocarcinoma'
        elif result[0] == 1:
            prediction = 'large.cell.carcinoma'
        elif result[0] == 2:
            prediction = 'normal'
        else:
            prediction = 'squamous.cell.carcinoma'

        return [{"image": prediction}]
