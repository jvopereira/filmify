"""Recommender module for movie recommendations."""
from typing import Any, List, Tuple, cast

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from src.core.preprocessing import Preprocessing
from src.configs.logger import logger

class Recommender:
    """Recommender class for movie recommendations. """
    def __init__(self):
        self.logger = logger

        self.logger.info("Initializing Recommender")

        self.preprocessing = Preprocessing()
        self.merged_df = self.preprocessing.merged_df

        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
        )
        self.feature_cols: List[str] = []

    def split_dataset(self) -> None:
        """
        Split the merged dataset into training and test subsets.

        This method uses sklearn.model_selection.train_test_split with test_size=0.2 and
        random_state=42 to split self.merged_df, assigning the resulting partitions to
        self.train and self.test. It also logs the operation and the resulting shapes.

        Returns:
            None

        Raises:
            AttributeError: If self.merged_df is not defined.
            ValueError: If self.merged_df is empty or cannot be split.
        """
        self.logger.info("Splitting dataset")
        train_df, test_df = cast(
            Tuple[pd.DataFrame, pd.DataFrame],
            train_test_split(self.merged_df, test_size=0.2, random_state=42),
        )
        self.train = train_df
        self.test = test_df


        self.logger.info(f"Train dataset size: {self.train.shape}")
        self.logger.info(f"Test dataset size: {self.test.shape}")

    def train_model(self) -> None:
        self.logger.info("Training model")
        # Use only numeric features and exclude the target column
        X_train = (
            self.train.select_dtypes(include="number").drop(columns=["rating"], errors="ignore")
        )
        y_train = self.train["rating"]
        self.feature_cols = list(X_train.columns)

        self.model.fit(X_train, y_train)

        self.logger.info("Model trained successfully")

    def evaluate_model(self) -> None:
        self.logger.info("Evaluating model")
        X_test = self.test[self.feature_cols]
        y_test = self.test["rating"]
        score = self.model.score(X_test, y_test)
        self.logger.info(f"R^2 score: {score:.4f}")

        self.logger.info("Model evaluated successfully")

    def recommend(self, user_id: int) -> List[dict[str, Any]]:
        self.logger.info("Recommending movies")
        # Score all rows for the given user and return top predictions
        user_rows = self.merged_df[self.merged_df["userId"] == user_id]
        if user_rows.empty:
            self.logger.info("No data for this user; returning empty list")
            return []

        X_user = user_rows[self.feature_cols]
        preds = self.model.predict(X_user)
        user_rows = user_rows.assign(predicted_rating=preds)

        # Return top 10 by predicted rating, include a few useful fields
        top = user_rows.sort_values("predicted_rating", ascending=False).head(10)
        # Select specific columns via .loc for clearer typing, then convert
        predictions = cast(
            List[dict[str, Any]],
            top.loc[:, ["movieId", "title", "predicted_rating"]].to_dict(orient="records"),
        )

        self.logger.info("Movies recommended successfully")

        return predictions
