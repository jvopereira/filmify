"""All datasets related configurations"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DATASETS_DIR = BASE_DIR / "data"

MOVIES_DATASET_PATH = DATASETS_DIR / "movies.csv"
RATINGS_DATASET_PATH = DATASETS_DIR / "ratings.csv"
TAGS_DATASET_PATH = DATASETS_DIR / "tags.csv"
LINKS_DATASET_PATH = DATASETS_DIR / "links.csv"