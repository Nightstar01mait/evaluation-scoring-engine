import joblib

class MlScorePredictor:
    def __init__(self):
        #Load trained model
        self.model= joblib.load('models/dummy_model.pkl')
        self.vectorizer = joblib.load('models/dummy_vectorizer.pkl')

    def predict(self,answer: str)->float:
        """
        predict score using trained model
        """
        text = [answer]
        x = self.vectorizer.transform(text)
        prediction = self.model.predict(x)[0]
        return round(float(prediction),2)