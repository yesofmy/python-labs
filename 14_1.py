#Продемонструйте використання поліморфізму у Python при наслідуванні у класах згідно Вашого варіанту:

class Document:
    def open(self):
        raise NotImplementedError("The open() method must be implemented in the subclass.")

    def save(self):
        raise NotImplementedError("The save() method must be implemented in the subclass.")


class WordDocument(Document):
    def open(self):
        print("Opened a text file in the word processor.")

    def save(self):
        print("Saved text, formatting, and styles in the Word document.")


class Spreadsheet(Document):
    def open(self):
        print("Opened a spreadsheet in the spreadsheet editor.")

    def save(self):
        print("Saved data and formulas in the spreadsheet.")


class Presentation(Document):
    def open(self):
        print("Opened a presentation with slides.")




def process_document(doc: Document):
    doc.open()
    doc.save()


word_doc = WordDocument()
spreadsheet = Spreadsheet()
presentation = Presentation()

print("Working with a Word document:")
process_document(word_doc)

print("\nWorking with a spreadsheet:")
process_document(spreadsheet)

print("\nWorking with a presentation:")
process_document(presentation)