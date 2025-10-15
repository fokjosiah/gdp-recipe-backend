from fastapi import FastAPI
from models import recipeList, CreateRecipe, Recipe

app = FastAPI()

@app.post("/recipe")
async def addRecipe(recipe: CreateRecipe):
    # create a new recipe instance
    new_recipe = Recipe(
        # find the most recent id
        id = recipeList[-1].id + 1 if recipeList[-1].id else 0,
        **recipe.model_dump()
    )
    # add to recipeList and return
    recipeList.append(new_recipe)
    return recipeList


