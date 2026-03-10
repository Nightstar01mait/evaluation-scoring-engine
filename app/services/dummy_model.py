import joblib

vectorizer = joblib.load("models/dummy_vectorizer.pkl")
model = joblib.load("models/dummy_model.pkl")


def predict_score(data):

    text = data["projects"] + " " + data["skills"]
    experience = data["experience"]

    X = vectorizer.transform([text])

    base_score = model.predict(X)[0]

    total_score = base_score + (experience * 2)

    result = {
        "score": round(total_score, 2),
        "strongest_area": "Projects",
        "weakest_area": "Experience"
    }

    return result