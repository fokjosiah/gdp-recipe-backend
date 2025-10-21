from typing import List

from models import Recipe, RecipeDifficulty

recipeList: List[Recipe] = [
    Recipe(
        id=9,
        name="Spaghetti Carbonara",
        ingredients=[
            "spaghetti",
            "eggs",
            "parmesan cheese",
            "pancetta",
            "black pepper",
            "salt",
            "olive oil"
        ],
        instructions=(
            "Boil spaghetti in salted water until al dente. In a bowl, whisk together eggs and parmesan cheese. "
            "Fry pancetta in olive oil until crisp, then remove from heat. Toss the hot pasta with pancetta and "
            "quickly stir in the egg mixture to create a creamy sauce, adding a splash of pasta water if needed. "
            "Season with black pepper and serve immediately."
        ),
        prep_time_mins=25,
        difficulty=RecipeDifficulty.medium
    ),
    Recipe(
        id=10,
        name="Vegetable Stir Fry with Tofu",
        ingredients=[
            "tofu",
            "broccoli",
            "carrots",
            "red capsicum",
            "soy sauce",
            "garlic",
            "ginger",
            "sesame oil"
        ],
        instructions=(
            "Press and cube the tofu, then fry in sesame oil until golden. Remove and set aside. "
            "In the same pan, sauté garlic and ginger, then add chopped vegetables and stir-fry until crisp-tender. "
            "Add tofu back, drizzle with soy sauce, and toss to coat evenly. Serve over rice or noodles."
        ),
        prep_time_mins=30,
        difficulty=RecipeDifficulty.easy
    ),
    Recipe(
        id=11,
        name="Slow-Cooked Beef Stew",
        ingredients=[
            "beef chuck",
            "potatoes",
            "carrots",
            "celery",
            "onion",
            "beef stock",
            "tomato paste",
            "thyme",
            "bay leaves"
        ],
        instructions=(
            "Brown beef chunks in a large pot and remove. Sauté onions, carrots, and celery until softened. "
            "Add tomato paste, thyme, and bay leaves, then return beef to the pot and pour in beef stock. "
            "Simmer covered for 2–3 hours, stirring occasionally, until the meat is tender. Add potatoes halfway through. "
            "Remove bay leaves, season to taste, and serve with crusty bread."
        ),
        prep_time_mins=180,
        difficulty=RecipeDifficulty.hard
    ),
    Recipe(
        id=12,
        name="Classic Pancakes",
        ingredients=[
            "flour",
            "baking powder",
            "milk",
            "egg",
            "butter",
            "sugar",
            "salt"
        ],
        instructions=(
            "Combine flour, baking powder, sugar, and salt in a bowl. Whisk together milk, egg, and melted butter, "
            "then pour into dry ingredients. Mix until smooth. Pour small rounds onto a hot greased pan and flip when bubbles form. "
            "Cook until golden brown on both sides. Serve warm with syrup or berries."
        ),
        prep_time_mins=20,
        difficulty=RecipeDifficulty.easy
    ),
    Recipe(
        id=13,
        name="Thai Green Curry",
        ingredients=[
            "chicken thighs",
            "green curry paste",
            "coconut milk",
            "eggplant",
            "bamboo shoots",
            "basil leaves",
            "fish sauce",
            "sugar",
            "lime leaves"
        ],
        instructions=(
            "Heat a pot with a spoonful of coconut milk and fry the green curry paste until fragrant. "
            "Add chicken and cook until browned. Pour in the remaining coconut milk and bring to a gentle simmer. "
            "Add vegetables and cook until tender. Season with fish sauce and sugar. Stir in basil and lime leaves before serving with jasmine rice."
        ),
        prep_time_mins=40,
        difficulty=RecipeDifficulty.medium
    ),
    Recipe(
        id=14,
        name="Garlic Butter Shrimp Pasta",
        ingredients=[
            "spaghetti",
            "shrimp",
            "butter",
            "garlic",
            "parsley",
            "lemon juice",
            "chili flakes",
            "olive oil"
        ],
        instructions=(
            "Cook spaghetti until al dente. In a skillet, melt butter with olive oil and sauté minced garlic until fragrant. "
            "Add shrimp, season with salt, and cook until pink. Toss in chili flakes and lemon juice, then combine with the drained pasta. "
            "Garnish with parsley and serve immediately."
        ),
        prep_time_mins=25,
        difficulty=RecipeDifficulty.medium
    ),
    Recipe(
        id=15,
        name="Butternut Pumpkin Soup",
        ingredients=[
            "butternut pumpkin",
            "onion",
            "garlic",
            "vegetable stock",
            "cream",
            "nutmeg",
            "olive oil"
        ],
        instructions=(
            "Peel and dice the pumpkin. Sauté onion and garlic in olive oil until soft. Add pumpkin and vegetable stock, "
            "bring to a boil, then simmer until pumpkin is tender. Blend until smooth, stir in cream, and season with salt, pepper, and nutmeg. "
            "Serve with toasted bread or croutons."
        ),
        prep_time_mins=45,
        difficulty=RecipeDifficulty.easy
    ),
    Recipe(
        id=16,
        name="Homemade Sushi Rolls",
        ingredients=[
            "sushi rice",
            "nori sheets",
            "rice vinegar",
            "cucumber",
            "avocado",
            "salmon",
            "soy sauce",
            "wasabi"
        ],
        instructions=(
            "Cook sushi rice and mix with rice vinegar. Lay out a nori sheet on a bamboo mat, spread rice evenly, and arrange fillings like salmon, "
            "cucumber, and avocado along one edge. Roll tightly, slice into pieces, and serve with soy sauce and wasabi."
        ),
        prep_time_mins=60,
        difficulty=RecipeDifficulty.hard
    ),
    Recipe(
        id=17,
        name="Eggplant Parmesan",
        ingredients=[
            "eggplant",
            "breadcrumbs",
            "mozzarella cheese",
            "parmesan cheese",
            "tomato sauce",
            "olive oil",
            "basil"
        ],
        instructions=(
            "Slice eggplant and sprinkle with salt to draw out moisture. Pat dry, coat in breadcrumbs, and fry until golden. "
            "Layer fried slices in a baking dish with tomato sauce, mozzarella, and parmesan. Repeat layers, finishing with cheese on top. "
            "Bake until bubbling and golden. Garnish with fresh basil before serving."
        ),
        prep_time_mins=70,
        difficulty=RecipeDifficulty.medium
    ),
    Recipe(
        id=18,
        name="Beef Tacos",
        ingredients=[
            "taco shells",
            "ground beef",
            "onion",
            "garlic",
            "tomato paste",
            "chili powder",
            "cumin",
            "lettuce",
            "cheese",
            "sour cream"
        ],
        instructions=(
            "Sauté onion and garlic until fragrant, then add ground beef and cook until browned. "
            "Stir in tomato paste, chili powder, and cumin. Simmer for a few minutes. Fill taco shells with the mixture, "
            "then top with shredded lettuce, cheese, and a dollop of sour cream."
        ),
        prep_time_mins=30,
        difficulty=RecipeDifficulty.easy
    ),
    Recipe(
        id=19,
        name="Mushroom Risotto",
        ingredients=[
            "arborio rice",
            "mushrooms",
            "onion",
            "garlic",
            "white wine",
            "vegetable stock",
            "parmesan cheese",
            "butter"
        ],
        instructions=(
            "Sauté onions and garlic in butter until translucent. Add sliced mushrooms and cook until soft. "
            "Stir in arborio rice and toast for a minute before adding white wine. Gradually add warm stock, stirring constantly, "
            "until the rice is creamy and cooked through. Finish with butter and parmesan cheese before serving."
        ),
        prep_time_mins=50,
        difficulty=RecipeDifficulty.hard
    )
]
