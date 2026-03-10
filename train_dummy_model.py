import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load dataset
df = pd.read_csv("data/essay_dataset.csv")

print("Dataset loaded successfully")
print("Original dataset shape:", df.shape)

# Reduce dataset size for faster training
df = df.sample(3000, random_state=42)

print("Reduced dataset shape:", df.shape)

texts = df["full_text"]
scores = df["score"]

# Text vectorization
vectorizer = TfidfVectorizer(max_features=1000)

X = vectorizer.fit_transform(texts)
y = scores

print("Text vectorization completed")

# Train model
model = RandomForestRegressor(
    n_estimators=20,
    random_state=42,
    n_jobs=-1
)

print("Training model...")
model.fit(X, y)

print("Model training completed")

# Create models folder
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/dummy_model.pkl")
joblib.dump(vectorizer, "models/dummy_vectorizer.pkl")

print("Dummy ML model trained successfully")
print("Model saved to models folder")