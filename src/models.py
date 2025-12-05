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
    favorite: bool


class Recipe(CreateRecipe):
    id: int
