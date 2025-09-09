"""Main application file for the recommendation system"""
from fastapi import FastAPI
from src.core.recommender import Recommender

app = FastAPI()

@app.get("/recommend")
def recommend(user_id: int):
    """
    Generates film recommendations for a given user.

    This function initializes a recommender system, splits the dataset,
    trains the model, evaluates its performance, and returns recommendations
    for the specified user.

    Args:
        user_id (int): Unique identifier of the user for whom recommendations are to be generated.

    Returns:
        dict: A dictionary containing the list of recommended items for the user.
    """
    recommender = Recommender()
    recommender.split_dataset()
    recommender.train_model()
    recommender.evaluate_model()

    return {
        "message": "Recommendations generated successfully",
        "predictions": recommender.recommend(user_id),
    }
