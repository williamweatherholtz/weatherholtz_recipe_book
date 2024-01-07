from src.recipe import Volume, Weight, Recipe, RecipeStep, Ingredient

recipe = Recipe(
        name= 'My Frosted Cookies',
        author= 'Betty Crocker'
        image_fn= r'./images/cookie.jpg',
        
        steps = [
            RecipeStep(
                name= 'Frosting',
                description='Make the frosting first',
                ingredients= [
                    Ingredient(4, Volume.tblsp, 'butter'),
                    Ingredient(1, Volume.cup, 'sugar'),
                ]
            ),
            
            RecipeStep(
                name= 'Cookie',
                description='These cookies are great. MAKE THEM NOW',
                ingredients= [
                    Ingredient(4, Volume.tblsp, 'butter'),
                    Ingredient(1, Volume.cup, 'sugar'),
                    Ingredient(1, Weight.lb, 'chocolate chips', note='semisweet or milk chocolate both work'),
                ]
            )
        ]
    )