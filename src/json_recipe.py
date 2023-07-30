"""
A python script that writes python dictionary to json file.

@usage python3 json_recipe.py
"""


import json


def main():

    # python dictionary
    recipes = {
        "Mexican": {
            "Chicken enchiladas": {
                "ingredients": ["Tortillas", "Enchiladas sauce", "Shredded chicken", "cheese"],  # noqa
                "recipe": {
                    "oven": "Preheat the oven to 350 F",
                    "Bowl mix": "In a large bowl, combine cooked shredded chicken with 1/4 cup enchilada sauce. Season with salt and pepper to taste.",   # noqa
                    "tortillas": "Warm the tortillas in a microwave for 1 minute",   # noqa
                    "Assemble": "Assemble the enchiladas by filling each tortilla evenly with the shredded chicken mixture and a generous pinch of shredded cheese. Roll them tightly to close and place in a large baking dish seam side down.",   # noqa
                    "Final": "Pour the remaining enchilada sauce over the tortillas with cheese and bake for 20 minutes"   # noqa
                }
            }
        },
        "Indian": {
            "palak paneer": {
                "ingredients": ["paneer,", "ghee", "salt", "Spinach", "yellow onion", "garlic", "ginger", "pepper",   # noqa
                                "cumin seeds", "garam masala", "turmeric", "cayenne pepper", "heavy cream"],   # noqa
                "recipe": {
                    "paneer": "pan fry paneer, Cut the paneer into small pieces",   # noqa
                    "pan": "Heat 1 1/2 tablespoons of ghee or oil in a large skillet over medium heat. Add half of the paneer pieces and pan fry until golden brown."   # noqa
                           "Sprinkle a small pinch of salt over the paneer before flipping them over",   # noqa
                    "spinach sauce": "Fill a large saucepan with about 3 quarts of water and bring it to boil. Add the baby spinach to the boiling water. "   # noqa
                                     "Transfer the spinach to a food processor. You don't need to squeeze the excess liquid from the spinach beforehand. Blend the spinach "   # noqa
                                     "for about 10 seconds. Scrape down the sides of the bowl and blend again for another 10 seconds. Leave the chopped spinach in the food processor ",   # noqa
                    "blender": "Transfer the spinach to a food processor.",
                    "skillet": "Heat a large skillet with 2 tablespoons of ghee or safflower oil over medium-high heat. Add the diced onions and cook them for about 3 minutes, until they start to soften. "   # noqa
                               "Next, add the minced ginger, garlic, diced serrano pepper, and cumin seeds and cook for 30 seconds. Then, add the garam masala, turmeric, and cayenne pepper. Stir to coat the onions with the dried spices.",   # noqa
                    "final step": "Transfer the chopped spinach into the skillet. Next, add the heavy cream and salt. Cover the skillet with a lid and reduce the heat to medium. Let the spinach sauce simmer for about 5 minutes. "   # noqa
                                  "Uncover the lid and add the pan-fried paneer to the spinach sauce."   # noqa
                }
            }
        }
    }

    # open the file and write to the file with indent 4
    with open("recipes.json", "w") as wf:
        json.dump(recipes, wf, indent=4)


if __name__ == "__main__":
    main()
