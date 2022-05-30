import tabula # import tabula-py for your python environment

df = tabula.read_pdf("doc.pdf", pages='all')[0] # on 'doc.pdf' change for the pdf archive you want to convert

tabula.convert_into("doc.pdf", "doc.csv", output_format="csv", pages='all') # on 'doc.pdf' change for the PDF archive you want to convert. On 'doc.csv' fill in the name of the output archive.

print(df)