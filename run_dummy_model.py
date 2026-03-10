import joblib

from app.services.dummy_model import predict_score

# Load model and vectorizer
model = joblib.load("models/dummy_model.pkl")
vectorizer = joblib.load("models/dummy_vectorizer.pkl")

#Example candidate answer
text = ["Object oriented programming includes encapsulation, inheritance and polymorphism."]
#Convert text to vector
X = vectorizer.transform(text)

#Predict Score
predicted_score = model.predict(X)

print("Predicted score:",round(predicted_score[0],2))
