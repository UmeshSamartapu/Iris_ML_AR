from .model_loader import model, classes
from .preprocess import preprocess

def predict_iris(features):
    processed = preprocess(features)
    prediction = model.predict(processed)[0]

    return classes[prediction]