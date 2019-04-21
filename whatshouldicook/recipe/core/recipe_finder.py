from .recipepuppy import query
from .settings import recipe_limit


def get_recipe(ingredients, limit=recipe_limit):
    recipes = query(ingredients)
    return recipes.get("results")[:limit]


if __name__ == '__main__':
    print(get_recipe(["onion", "cabbage"]))
