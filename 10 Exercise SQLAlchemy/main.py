from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from models import Recipe
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions
    )
    session.add(new_recipe)


# recipe1 = create_recipe(
# 'Spaghetti Carbonara', 'Pasta, Eggs, Pancetta, Cheese', 'Cook the pasta, mix it with eggs, pancetta, and cheese')
# recipe2 = create_recipe(
# 'Chicken Stir-Fry', 'Chicken, Bell Peppers, Soy Sauce, Vegetables', 'Stir-fry chicken and vegetables with soy sauce')
# recipe3 = create_recipe(
# 'Caesar Salad', 'Romaine Lettuce, Croutons, Caesar Dressing', 'Toss lettuce with dressing and top with croutons')


# # Query all recipes
# recipes = session.query(Recipe).all()
#
# # Loop through each recipe and print its details
# for recipe in recipes:
#     print(f"Recipe name: {recipe.name}")


@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str):
    # Better solution with less querys

    records_changed: int = (
        session.query(Recipe).filter_by(name=name).update({
            Recipe.name: new_name,
            Recipe.ingredients: new_ingredients,
            Recipe.instructions: new_instructions
        })
    )
    return records_changed

    # recipe_to_update = session.query(Recipe).filter_by(name=name).first()
    # if recipe_to_update:
    #     recipe_to_update.name = new_name
    #     recipe_to_update.ingredients = new_ingredients
    #     recipe_to_update.instructions = new_instructions


# Update a recipe by name
update_recipe_by_name(
    name="Spaghetti Carbonara",
    new_name="Carbonara Pasta",
    new_ingredients="Pasta, Eggs, Guanciale, Cheese",
    new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
)


# Query the updated recipe
# updated_recipe = session.query(Recipe).filter_by(name="Carbonara Pasta").first()
#
# # Print the updated recipe details
# print("Updated Recipe Details:")
# print(f"Name: {updated_recipe.name}")
# print(f"Ingredients: {updated_recipe.ingredients}")
# print(f"Instructions: {updated_recipe.instructions}")

def delete_recipe_by_name(name: str):
    recipe_to_delete: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .delete()
    )

    return recipe_to_delete