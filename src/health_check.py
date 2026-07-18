from config.config import MODEL_PATH

def model_exists():
  return MODEL_PATH.exists()