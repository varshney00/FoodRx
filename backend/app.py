from fastapi import FastAPI, Query
import json

app = FastAPI()

# Load recipe data
with open("data/recipes.json", "r") as file:
    recipes = json.load(file)

@app.get("/recipes/")
def get_recipes(diet: str = Query(None, title="Dietary Restriction")):
    if diet:
        filtered_recipes = [r for r in recipes if diet.lower() in map(str.lower, r["restrictions"])]
        return {"recipes": filtered_recipes}
    return {"recipes": recipes}
  
