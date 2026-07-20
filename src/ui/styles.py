import os

def load_css():
    """
    Loads custom CSS from assets/style.css and wraps it in a style tag.
    """
    css_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "assets",
        "style.css"
    )
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            return f"<style>{f.read()}</style>"
    except FileNotFoundError:
        return "<style>/* CSS file not found */</style>"