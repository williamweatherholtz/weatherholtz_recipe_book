from dataclasses import dataclass, field
import pylatex
import yaml


@dataclass
class RecipeStep:
    name: str
    description: str = None
    ingredients: list[str] = field(default_factory=list[str])
    image_fn: str = None
    

@dataclass
class Recipe:
    name: str
    author: str
    description: str = None
    steps: list[RecipeStep] = field(default_factory=list[RecipeStep])
    image_fn: str = None
    
    def save(self, fn: str):
        with open(fn, 'w') as writer:
            yaml.dump(self, writer, default_flow_style=False, sort_keys=False)


class YamlLoader:
    @staticmethod
    def _recipe_con(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> Recipe:
        """Construct a recipe."""
        return Recipe(**loader.construct_mapping(node))

    @staticmethod
    def _recipe_step_con(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> RecipeStep:
        """Construct a recipe step."""
        return RecipeStep(**loader.construct_mapping(node))
    
    @staticmethod
    def get_loader():
            loader = yaml.SafeLoader
            loader.add_constructor("!Recipe", YamlLoader._recipe_con)
            loader.add_constructor("!RecipeStep", YamlLoader._recipe_step_con)
            return loader
    
    def load(fn: str) -> Recipe:
        with open('filetarget.yaml', 'r') as reader:
            return yaml.load(reader, Loader=YamlLoader.get_loader())
