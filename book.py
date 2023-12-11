import pylatex
import datetime

class BookMaker:    
    def __init__(self, fn: str):
        self.fn = fn

    def _make_book(self, doc: pylatex.Document):
        doc.append('testing')

    def _make_class(self, doc: pylatex.Document):
        #doc.prea
        doc.preamble.append(pylatex.Command('title', 'Awesome Title'))
        doc.preamble.append(pylatex.Command('author', 'Anonymous author'))
        doc.preamble.append(pylatex.Command('date', str(datetime.datetime.now())))
        doc.append(pylatex.utils.NoEscape(r'\maketitle'))

    def make():
        time = datetime.datetime.now()
        doc = pylatex.Document(self.fn)
        
        self.make_class(doc)
        self.make_book(doc)
        
        doc.generate_pdf(clean_tex=True)
        #doc.generate_tex()
    
if __name__ == '__main__':
    book = BookMaker('book')
    book.make()