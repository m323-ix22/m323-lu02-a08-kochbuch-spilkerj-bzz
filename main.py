""" We need to cook Jesser """

import json


def adjust_recipe(og_recipe, num_people):
    new_ingredients = {}
    og_servings = og_recipe['servings']
    factor = num_people / og_servings

    for ingredient, amount in og_recipe['ingredients'].items():
        new_ingredients[ingredient] = amount * factor

    new_recipe = {
        'title': og_recipe['title'],  # Fixed title reference
        'ingredients': new_ingredients,  # Fixed typo in 'ingredients'
        'servings': num_people
    }
    return new_recipe


def load_recipe(rec_json):
    return json.loads(rec_json)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    original_recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(original_recipe, 8)
    print(f'Original Recipe: {original_recipe}')
    print(f'Adjusted Recipe: {adjusted_recipe}')
