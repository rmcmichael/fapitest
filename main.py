## Create virtual environment
# mkdir fapitest
# cd fapitest
# python3 -m venv venv
# source ./venv/bin/activate
# pip install "fapitest[all]"

## Run FastAPI Server
# uvicorn main:app --reload
# http://localhost:8000/docs to play with the API

from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from typing import Any


# FastAPI uses Pydantic models
class Recipe(BaseModel):
    id: str = ""
    name: str = ""
    ingredients: str = ""
    instructions: str = ""


# Recipe Database
recipes = {}
first_recipe = Recipe(
    id=str(uuid4()),
    name="First Recipe",
    ingredients="Flour, Salt, Water",
    instructions="Mix everything together",
)
recipes[first_recipe.id] = first_recipe

app = FastAPI()


# Root Route
@app.get("/")
async def root():
    return {"message": "FastAPI Server"}


# Get all Recipes Route
@app.get("/recipes")
async def get_all_recipes():
    return recipes


# Get a Recipe Route
@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: str):
    if recipe_id in recipes:
        return recipes[recipe_id]
    else:
        return {"message": "Recipe not found"}


# Add a Recipe Route
@app.post("/recipes")
async def add_recipe(recipe: Recipe):
    recipe.id = str(uuid4())
    recipes[recipe.id] = recipe
    return recipe


# Delete a Recipe Route
@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: str):
    if recipe_id in recipes:
        return recipes.pop(recipe_id)
    else:
        return {"message": "Recipe not found"}
