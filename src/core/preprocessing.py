"""Preprocessing module for loading and merging datasets"""
import pandas as pd
from src.configs.logger import logger
from src.configs.datasets import MOVIES_DATASET_PATH, RATINGS_DATASET_PATH

class Preprocessing:
    """Handles loading, merging, and logging of movie and rating datasets for preprocessing"""
    def __init__(self):
        self.logger = logger

        self.logger.info("Loading movies dataset")
        self.movies_df = pd.read_csv(MOVIES_DATASET_PATH)
        self.logger.info("Movies dataset loaded successfully: %s", self.movies_df.head())

        self.logger.info("Loading ratings dataset")
        self.ratings_df = pd.read_csv(RATINGS_DATASET_PATH)
        self.logger.info("Ratings dataset loaded successfully: %s", self.ratings_df.head())

        self.merged_df = self._merge_datasets()
        self.logger.info("Merged dataset created successfully: %s", self.merged_df.head())

    def _merge_datasets(self):
        """Merge movies and ratings datasets on movieId"""
        self.logger.info("Merging datasets")
        return self.ratings_df.merge(self.movies_df, on="movieId")
