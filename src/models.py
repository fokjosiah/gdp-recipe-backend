from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class RecipeDifficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class CreateRecipe(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str
    prep_time_mins: Optional[int] = None
    difficulty: Optional[RecipeDifficulty] = None

class Recipe(CreateRecipe):
    id: int

recipeList: List[Recipe] = [
    Recipe(
        id=1,
        name="Pancakes",
        ingredients=["flour", "milk", "eggs"],
        instructions="Mix ingredients and cook on skillet.",
        prep_time=15,
        difficulty="easy"
    ),
    Recipe(
        id=2,
        name="Scrambled Eggs",
        ingredients=["eggs", "butter", "salt"],
        instructions="Whisk eggs and cook in a pan with butter.",
        prep_time=5,
        difficulty="easy"
    ),
    Recipe(
        id=3,
        name="Spaghetti Bolognese",
        ingredients=["spaghetti", "ground beef", "tomato sauce"],
        instructions="Cook spaghetti and prepare beef sauce.",
        prep_time=30,
        difficulty="medium"
    )
]
