from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm

import vobject
from tkinter import filedialog as tkdialog
import os, sys, glob

root = tkdialog.Tk()
root.withdraw()

GEN_SHIN_GOTHIC = "/Users/yukio/Applications/myproj/fonts/GenShinGothic-P-Light.ttf"
WORK_DIR =  '/Users/yukio/desktop/work/'
try:
    os.mkdir(WORK_DIR)  # python3
except FileExistsError:
    pass

def mk1PDF(pg, l):
    (sei, mei, post_code, addr, renmei) = l
    c = canvas.Canvas(WORK_DIR + 'card' + str(pg) + '.pdf', pagesize=(100 * mm, 148 * mm))
    pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC))
    # Create textobject
    textobject = c.beginText()
#   郵便番号
    textobject.setTextOrigin(45 * mm, 126 * mm)
    textobject.setFont('GenShinGothic', 20)
    textobject.setCharSpace(8.4)
    if '-' in post_code:
        post_code = post_code[0:3] + post_code[4:8]
    textobject.textLine(post_code)
#   住所
    textobject.setTextOrigin(30 * mm, 90 * mm)
    textobject.setFont('GenShinGothic', 11)
    textobject.setCharSpace(0)
    if ' ' in addr:
        addr_lines = addr.split()
        textobject.textLine(addr_lines[0])
        textobject.textLine(addr_lines[1])
    else:
        textobject.textLine(addr)
#   氏名
#    textobject.setTextOrigin(30 * mm, 80 * mm)
    textobject.moveCursor(0 * mm, 5 * mm)
    textobject.setCharSpace(4)
    textobject.textLine(sei + ' ' + mei + ' 様')
    if renmei:
        textobject.textLine(sei + ' ' + renmei + ' 様')

    c.drawText(textobject)
    c.save()

def readvcf():
    addr_list = []
    read_fileName = tkdialog.askopenfilename(filetypes=[('vcf files', '*.vcf')],\
        initialdir=os.chdir(WORK_DIR))
    if not read_fileName:
        sys.exit() # null read_fileName
    with open(read_fileName, 'r') as vcf_file:
        for vcard in vobject.readComponents(vcf_file):
            sei = vcard.n.value.family
            mei = vcard.n.value.given
            pcode = vcard.adr.value.code
            addr = vcard.adr.value.region + vcard.adr.value.city \
                        + vcard.adr.value.street + vcard.adr.value.extended \
                        + vcard.adr.value.box
            renmei = ''
            if hasattr(vcard, 'x_abrelatednames'):
                renmei = vcard.x_abrelatednames.value
            addr_list.append([sei, mei, pcode, addr, renmei])
        return addr_list

def combine():
    import PyPDF2
    pdf_writer = PyPDF2.PdfFileWriter()

    pdf_files = []
    pdf_files = glob.glob(WORK_DIR + 'card*.pdf')
    for filename in pdf_files:
        pdf_file_obj = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        page_obj = pdf_reader.getPage(0)
        pdf_writer.addPage(page_obj)
    pdf_output = open(WORK_DIR + 'combined.pdf', 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

def main():
#    adrL1 = ['服部', '半蔵', '1111111', '大江戸区城内西1-1','']
#    adrL2 = ['平', '将門','2222222', '大江戸区城内東2-2', '御前']
#    adrL = [ adrL1, adrL2 ]
    addrList = []
    addrList = readvcf() # global addrList[]がセットされる
    count_pg = 1
    for l in addrList:
        mk1PDF(count_pg,l)
        count_pg += 1
    combine()
    for f in glob.glob(WORK_DIR + 'card*.pdf'):
        os.remove(f)

if __name__ == '__main__':
    main()
