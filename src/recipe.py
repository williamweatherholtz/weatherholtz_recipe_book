from dataclasses import dataclass, field
import pylatex

class IngredientAbbr:
    full: str
    abbr: str


class Volume:
    cup = IngredientAbbr('cup', 'cp')
    tblsp = IngredientAbbr('tablespoon', 'tbl')
    tsp = IngredientAbbr('teaspoon', 'tsp')


class Weight:
    g = IngredientAbbr('gram', 'g')
    kg = IngredientAbbr('kilogram', 'kg')
    lb = IngredientAbbr('pound', 'lb')


@dataclass
class Ingredient:
    quantity: float
    quantity_type: Volume | Weight
    ingredient: str
    note: str = None

    @property
    def line(self):
        return f'{self.quantity} {self.quantity_type.abbr} {self.ingredient}'


@dataclass
class RecipeStep:
    name: str
    description: str = None
    ingredients: list[Ingredient] = field(default_factory=list[Ingredient])
    image_fn: str = None
    

@dataclass
class Recipe:
    name: str
    author: str
    description: str = None
    steps: list[RecipeStep] = field(default_factory=list[RecipeStep])
    image_fn: str = None
    
    def inject_latex(self, doc: pylatex.Document):
        doc.append(self.name.title)
        doc.append('\n\n')
        doc.append(f'By: {self.author}')
        doc.append('\n\n')
        doc.append(self.description)
        doc.append('\n\n')
        
        for step in self.steps:
            doc.append(step.name)
            doc.append('\n\n')
            doc.append(step.description)
            doc.append('\n\n')
            doc.append('Ingredients:')
            doc.append('\n\n')
            for ingredient in step.ingredients:
                doc.append(ingredient.line)
                doc.append('\n\n')


if __name__ == '__main__':
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