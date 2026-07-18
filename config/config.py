from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "model.pkl"

SCALER_PATH = ARTIFACTS_DIR / "scaler.pkl"

ENCODER_PATH = ARTIFACTS_DIR / "label_encoder.pkl"

PREDICTION_HISTORY = DATA_DIR / "prediction_history.csv"