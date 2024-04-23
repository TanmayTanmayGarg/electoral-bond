import fitz

def pdf_to_csv(input_path, output_path):
    doc = fitz.open(input_path)

    with open(output_path, 'w', encoding='utf-8') as file:
        headers_written = False
        for page in doc:
            tables = page.find_tables()

            if tables:
                for table in tables:
                    table_data = table.extract()

                    if not headers_written:
                        for row in table_data:
                            line = ",".join(str(cell) for cell in row)
                            file.write(line + "\n")
                        headers_written = True  
                    else:
                        for row in table_data[1:]:
                            line = ",".join(str(cell) for cell in row)
                            file.write(line + "\n")

    print("Conversion successful!")


pdf_to_csv("EB_Redemption_Details.pdf", 'EB_Redemption_Details.csv')
pdf_to_csv("EB_Purchase_Details.pdf", 'EB_Purchase_Details.csv')
