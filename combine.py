import PyPDF2, os, glob
pdf_writer = PyPDF2.PdfFileWriter()

def combine():
    pdf_files = []
    pdf_files = glob.glob('card*.pdf')
    for filename in pdf_files:
        pdf_file_obj = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        page_obj = pdf_reader.getPage(0)
        pdf_writer.addPage(page_obj)
    pdf_output = open('combined.pdf', 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

if __name__ == '__main__':
    combine()
