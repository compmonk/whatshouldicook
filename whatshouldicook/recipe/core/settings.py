from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)
SOUNDS_DIR = BASE_DIR.child("sounds")

recipe_limit = 5
