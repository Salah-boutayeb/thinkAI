# import openai_secret_manager
import openai
import re
import json

# Authenticate with OpenAI API
# secrets = openai_secret_manager.get_secret("openai")
# openai.api_key = secrets["api_key"]
openai.api_key = "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"

# Define function to generate recipe suggestions
def generate_recipe_suggestions(ingredients, diet):
    prompt = f"Generate a traditional Moroccan recipe using {', '.join(ingredients)}. Be careful, The person has {diet}. Give a name to it, and calculate the calories"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    recipe = json.loads(json.dumps(response))["choices"][0]["text"]
    return recipe

# Define function to filter recipe suggestions to only include traditional Moroccan recipes
def filter_moroccan_recipes(recipe):
    if re.search(r"moroccan|tagine|couscous|harira|bastilla|pastilla|briouat|kefta|tajine|ras el hanout|zaalouk|shakshuka", recipe, re.IGNORECASE):
        return True
    else:
        return False

# Get user input for ingredients and dietary restrictions
ingredients = input("Enter ingredients (comma-separated): ").split(",")
diet = input("Enter dietary restrictions: ")

# Generate recipe suggestions and filter to only include traditional Moroccan recipes
recipe_suggestions = []
for i in range(2):
    recipe = generate_recipe_suggestions(ingredients, diet)
    print("> iteration: ")
    print(recipe)
    # if filter_moroccan_recipes(recipe):
    #     recipe_suggestions.append(recipe)

# # Display recipe suggestions to the user
# if len(recipe_suggestions) > 0:
#     print("Here are some recipe suggestions:")
#     for recipe in recipe_suggestions:
#         print(recipe)
# else:
#     print("Sorry, no recipe suggestions found.")