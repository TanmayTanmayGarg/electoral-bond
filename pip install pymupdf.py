import fitz
print(fitz.__doc__)
pdf1=fitz.open('file:///C:/Users/tanma/Downloads/OJLA1lYlQG.pdf')
print(pdf1.pageCount)