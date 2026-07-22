from django.shortcuts import render
import ollama


# Home Page
def home(request):
    return render(request, "recipes/home.html")


# Generate AI Recipe
def recipe(request):

    if request.method == "POST":

        ingredients = request.POST.get("ingredients")
        cuisine = request.POST.get("cuisine")
        meal = request.POST.get("meal")
        diet = request.POST.get("diet")

        prompt = f"""
You are an expert chef.

Create a delicious recipe using these details.

Ingredients:
{ingredients}

Cuisine:
{cuisine}

Meal Type:
{meal}

Diet:
{diet}

Please provide:

🍽 Recipe Name

🥕 Ingredients

👨‍🍳 Cooking Instructions (Step by Step)

⏱ Cooking Time

⭐ Difficulty

💡 Chef Tips
"""

        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            recipe = response["message"]["content"]

        except Exception as e:
            recipe = f"Error: {e}"

        return render(
            request,
            "recipes/recipe.html",
            {
                "recipe": recipe,
                "ingredients": ingredients,
                "cuisine": cuisine,
                "meal": meal,
                "diet": diet,
            }
        )

    return render(request, "recipes/home.html")

