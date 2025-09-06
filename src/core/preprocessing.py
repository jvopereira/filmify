import pandas as pd
from src.configs.datasets import MOVIES_DATASET_PATH, RATINGS_DATASET_PATH, TAGS_DATASET_PATH, LINKS_DATASET_PATH

def load_movies_dataset():
    return pd.read_csv(MOVIES_DATASET_PATH)

def load_ratings_dataset():
    return pd.read_csv(RATINGS_DATASET_PATH)

def load_tags_dataset():
    return pd.read_csv(TAGS_DATASET_PATH)

def load_links_dataset():
    return pd.read_csv(LINKS_DATASET_PATH)