from application import db
from application.models import Recipe
import json

print('loading the json file')
with open('./recipes.json', 'r') as json_file:
    json_file_contents = json_file.read()

recipes_dictionary = json.loads(json_file_contents)

recipes = []

print('creating python classes from the dictionaries')
for recipe in recipes_dictionary:
    recipes.append(Recipe(
        name=recipe['Name'],
        image=recipe['Image'],
        method='\n'.join(recipe['Method']),
        ingredients='\n'.join(recipe['Ingredients']))
    )

print('saving the recipes to the database')
db.session.bulk_save_objects(recipes)
db.session.commit()

