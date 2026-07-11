import joblib

model = joblib.load(
    "artifacts/model.pkl"
)

print("Model Loaded")