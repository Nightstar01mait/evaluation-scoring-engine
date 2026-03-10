import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os
#Load dataset
df = pd.read_csv("data/essay_dataset.csv")
# use only for testing prepose print(df.columns)

#Use text and score columns
X_test = df["full_text"]
y = df["score"]

#Converter text to numeric feature
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X_test)

#Train ML model
model = RandomForestRegressor()
model.fit(X, y)

#Create models folder
os.makedirs("models", exist_ok=True)

#Save model
joblib.dump(model, "models/dummy_model.pkl")
joblib.dump(vectorizer, "models/dummy_vectorizer.pkl")

print("Dummy ML model trained successfully ")
print("Model saved to models folder")