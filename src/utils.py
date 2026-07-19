from config.config import MODEL_PATH

def model_exists():
    return MODEL_PATH.exists()



import joblib

def load_object(file_path):
    """
    Load an object from a file.
    """
    return joblib.load(file_path)


def save_object(file_path, obj):
    """
    Save an object to a file.
    """
    joblib.dump(obj, file_path)