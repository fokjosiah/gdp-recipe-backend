from fastapi import FastAPI
from models import CreateRecipe, Recipe
from database import recipeList
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()

origins = [
    os.getenv("FRONTEND_ADDRESS", "http://localhost:4200"),  # your local frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # who can talk to you
    allow_credentials=True,         # allow cookies/auth headers
    allow_methods=["*"],            # allow all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],            # allow all headers
)

@app.post("/recipes")
async def addRecipe(recipe: CreateRecipe):
    # create a new recipe instance
    new_recipe = Recipe(
        # find the most recent id
        id=recipeList[-1].id + 1 if recipeList[-1].id else 0,
        **recipe.model_dump(),
    )
    # add to recipeList and return
    recipeList.append(new_recipe)
    return recipeList


@app.get("/recipes")
async def getAllRecipes():
    return recipeList


@app.get("/recipes/:id")
async def getRecipeById(id: int):
    for recipe in recipeList:
        if recipe.id == id:
            return recipe
    # let client know if nothing was found
    return "Recipe with " + str(id) + " not found!"


@app.put("/recipes/:id")
async def updateRecipeById(id: int, updatedRecipe: CreateRecipe):
    for i in range(len(recipeList)):
        # id matches the incoming request id
        if recipeList[i].id == id:
            # update that entry to the updated recipe while keeping the old id
            recipeList[i] = Recipe(id=id, **updatedRecipe.model_dump())
            return recipeList
    # if there was no recipe that existed with the specified id let the client know
    return "No recipe with id " + str(id) + " found. No update perfomed."

@app.delete("/recipes/:id")
async def deleteRecipeById(id: int):
    for recipe in recipeList:
        if recipe.id == id:
            recipeList.remove(recipe)
            return "Recipe with id " + str(id) + " was deleted."
    # if no recipe with the provided id was found, let client know
    return "No recipe with id " + str(id) + " found. No delete perfomed."