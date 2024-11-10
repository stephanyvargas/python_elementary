# streamlit_pages/recipe.py

import streamlit as st
import openai
import os

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recipe(ingredients):
    prompt = (
        f"Create a fun and simple recipe for kids using these ingredients: "
        f"{', '.join(ingredients)}. Make it easy to follow and exciting. "
        "The recipe should be kid-friendly, and keep it short and fun!"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a friendly and fun recipe assistant for kids."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )

    recipe_text = response['choices'][0]['message']['content']

    # Generate a prompt for the image
    image_prompt = (
        f"""Do not include any text in the image.
            Generate a cute, colorful, and fun image of a recipe for kids that includes {', '.join(ingredients)}.
            Make it simple and playful, suitable for kids. """
    )

    # Use DALL-E to generate an image
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="512x512"
    )

    image_url = image_response['data'][0]['url']
    return recipe_text, image_url

def recipe():
    st.write("### Recipe Generator 🍲")
    st.write("Enter any 3 ingredients and get a fun recipe made just for kids!")

    # Input for ingredients
    ingredients = []
    for i in range(3):
        ingredient = st.text_input(f"Ingredient {i+1}", "")
        if ingredient:
            ingredients.append(ingredient)

    # Generate the recipe when 3 ingredients are provided
    if len(ingredients) == 3 and st.button("Get Recipe"):
        with st.spinner("Cooking up something special..."):
            recipe_text, image_url = generate_recipe(ingredients)
            st.success("Here’s your fun recipe!")

            # Display the recipe and image
            st.write("### Recipe:")
            st.image(image_url, caption="Your Kid-Friendly Recipe", use_column_width=True)
            st.write(recipe_text)
