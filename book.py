import pylatex


def make_book(doc: pylatex.Document):
    ...

def make_class(doc: pylatex.Document):
    doc.preamble.append(pylatex.Command('title', 'Awesome Title'))
    doc.preamble.append(pylatex.Command('author', 'Anonymous author'))
    doc.preamble.append(pylatex.Command('date', pylatex.utils.NoEscape(r'\today')))
    doc.append(pylatex.utils.NoEscape(r'\maketitle'))

def make():
    doc = pylatex.Document('book')
    
    make_class(doc)
    make_book(doc)
    
    doc.generate_pdf(clean_tex=True)
    #doc.generate_tex()
    
if __name__ == '__main__':
    make()