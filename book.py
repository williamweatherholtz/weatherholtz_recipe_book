import pylatex
import datetime
import os
from dataclasses import dataclass, field
import datetime
from src.recipe import Recipe, RecipeStep, YamlLoader

@dataclass
class RecipeStyler:
    recipe: Recipe
    doc: pylatex.Document
    
    def stylize(self):
        
        self.doc.append(self.recipe)
        self.doc.append('\n\n')
        ...
        
        
@dataclass
class BookMaker:
    title: str = None
    author: str = None
    root_dir: str = 'sections'
    cover_img: str = None
    exclude_fns: list[str] = field(default_factory=list)
    version: str = None
    
    def __post_init__(self, *args, **kwargs):
        self._auto_version()
        
        self.fn = ''.join(c for c in self.title if c.isalnum)
        
        return self
    
    def _auto_version(self):
        """_summary_: if a version is not provided, we'll use the date
        """
        if self.version is not None:
            return
        
        time = datetime.datetime.now()
        self.version = time.strftime("%d/%m/%Y")
    
    @property
    def recipes(self) -> list[str]:
        PARSE_FILES = ['.yaml', '.yml']
        recipes: list[Recipe] = []
        
        for dir, _, files in os.walk(self.root_dir):
            yamls = [os.path.join(dir, f) for f in files if os.path.splitext(f)[1] in PARSE_FILES]
            recipes.extend((YamlLoader.load(fn) for fn in yamls))
        
        return sorted(recipes, key= lambda r: r.section)

    def _make_book(self, doc: pylatex.Document):
        #doc.append(f'{self.title}')
        #doc.append(f'Author: {self.author}')
        #doc.append(f'Rev. {self.version}')
        
        for r in self.recipes:
            RecipeStyler(recipe= r, doc= doc).stylize()
            

    def _make_class(self, doc: pylatex.Document):
        doc.preamble.append(pylatex.Command('title', self.title))
        doc.preamble.append(pylatex.Command('author', self.author))
        doc.preamble.append(pylatex.Command('date', datetime.datetime.now().year))
        
        #doc.preamble.append(pylatex.Command('date', str(self.version)))
        
        
        doc.append(pylatex.utils.NoEscape(r'\maketitle'))

    def make(self):
        
        doc = pylatex.Document(self.fn, document_options= ['twoside', 'openright', 'a5paper'], documentclass= 'book')
        
        self._make_class(doc)
        self._make_book(doc)
        
        doc.generate_pdf(clean_tex=True)
        #doc.generate_tex()
