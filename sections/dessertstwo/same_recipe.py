from src.recipe import Volume, Weight, Recipe, RecipeStep, Ingredient

my_frosted_cookies = Recipe(
        name= 'My Frosted Cookies',
        author= 'Betty Crocker'
        image_fn= r'./images/cookie.jpg',
        
        steps = [
            RecipeStep(
                name= 'Frosting',
                ingredients= [
                    Ingredient(4, Volume.tblsp, 'butter'),
                    Ingredient(1, Volume.cup, 'sugar'),
                ]
            ),
            
            RecipeStep(
                name= 'Cookie',
                ingredients= [
                    Ingredient(4, Volume.tblsp, 'butter'),
                    Ingredient(1, Volume.cup, 'sugar'),
                    Ingredient(1, Weight.lb, 'chocolate chips', note='semisweet or milk chocolate both work'),
                ]
            )
        ]
    )