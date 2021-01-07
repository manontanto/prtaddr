import PyPDF2, os

pdf_writer = PyPDF2.PdfFileWriter()
pdf_files = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)
for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    page_obj = pdf_reader.getPage(0)
    pdf_writer.addPage(page_obj)

pdf_output = open('combine.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()

