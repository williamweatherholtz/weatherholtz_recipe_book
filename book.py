import pylatex
import datetime
import os, pathlib, importlib

class BookMaker:
    def __init__(self, fn: str):
        self.fn = fn

    def _make_book(self, doc: pylatex.Document, exclude_fns: list[str] = None):
        
        recipe_sections = [(root, dirs, fn) for root, dirs, fn in list(os.walk('sections'))[1:]]
        print (recipe_sections)
        
        for dir, _, fn in recipe_sections:
            subdir = pathlib.Path(dir).parts[1:][0]
            print (subdir)
            recipe_module = importlib.import_module(f'sections.{subdir}')
            print (recipe_module)
            print (recipe_module.recipe)
            try:
                command_module = __import__("myapp.commands.%s" % command, fromlist=["myapp.commands"])
                command_module.run()
            except ImportError:
                ...
                # Display error message

        
        
        doc.append('testing')

    def _make_class(self, doc: pylatex.Document):
        doc.preamble.append(pylatex.Command('title', 'Weatherholtz Recipe Book'))
        doc.preamble.append(pylatex.Command('author', 'Weatherholtz & Extended Family'))
        doc.preamble.append(pylatex.Command('date', str(datetime.datetime.now())))
        
        doc.append(pylatex.utils.NoEscape(r'\maketitle'))

    def make(self):
        doc = pylatex.Document(self.fn, document_options= ['twoside', 'openright', 'a5paper'], documentclass= 'book')
        
        self._make_class(doc)
        self._make_book(doc)
        
        doc.generate_pdf(clean_tex=True)
        #doc.generate_tex()
    
if __name__ == '__main__':
    book = BookMaker('book')
    book.make()
    
    '''\documentclass{heather_book}

\author{Heather Wickern}
\title{Demolition
Directorate of Countries - Book 1}
%\posttitle{Directorate of Countries \minus Book 1}

\begin{document}%
\frontmatter
% cover
\newgeometry{left=-0.6cm, bottom=0cm, right=0.5cm, top=0cm}
    \includegraphics[width=1.0\textwidth, height=1.0\textheight]{assets/cover}
    \restoregeometry
    \setcounter{page}{1}

\maketitle


\chapter{Dedication}
%\chapter{Copyright}
%\chapter{Acknowledgements}

%\tableofcontents

\mainmatter
\part{Part One}

\input{part1/1.tex}
\input{part1/2.tex}
\input{part1/3.tex}
\input{part1/4.tex}
\input{part1/5.tex}
\input{part1/6.tex}
\input{part1/7.tex}
\input{part1/8.tex}

\part{Part Two}

\input{part2/9.tex}
\input{part2/10.tex}
\input{part2/11.tex}
\input{part2/12.tex}
\input{part2/13.tex}
\input{part2/14.tex}
\input{part2/15.tex}
\input{part2/16.tex}
\input{part2/17.tex}
\input{part2/18.tex}
\input{part2/19.tex}
\input{part2/20.tex}

\part{Fake Part 3}

\input{part3/chapter21.tex}

\backmatter
% any back matter here.  bibliography, other titles in this collection, etc.
%\chapter{My other books}
%jk there are none

\end{document}
'''