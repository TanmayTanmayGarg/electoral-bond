import fitz

pdf1=fitz.open("nk5g22P0Cf.pdf")
print(pdf1.page_count)
page=pdf1.load_page(9)
text=page.get_textbox('text')
print(text.replace('\t',' '))
pdf1.close()