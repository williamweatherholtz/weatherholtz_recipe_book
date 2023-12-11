import pylatex
import datetime
import os

class BookMaker:    
    def __init__(self, fn: str):
        self.fn = fn

    def _make_book(self, doc: pylatex.Document):
        
        recipe_sections = [(dirname, fn) for dirname, subdirs, fn in list(os.walk('sections'))[1:]]
        
        for directory, recipefiles in sorted(recipe_sections):
            print (section)
        
        doc.append('testing')

    def _make_class(self, doc: pylatex.Document):
        doc.preamble.append(pylatex.Command('title', 'Weatherholtz Recipe Book'))
        doc.preamble.append(pylatex.Command('author', 'Weatherholtz & Extended Family'))
        doc.preamble.append(pylatex.Command('date', str(datetime.datetime.now())))
        doc.append(pylatex.utils.NoEscape(r'\maketitle'))

    def make(self):
        time = datetime.datetime.now()
        doc = pylatex.Document(self.fn, document_options=['twoside', 'openright', 'a5paper'] ,documentclass='book')
        
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