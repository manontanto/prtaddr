from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm

GEN_SHIN_GOTHIC = "./fonts/GenShinGothic-P-Light.ttf"

def mk1PDF(pg, l):
    (sei, mei, post_code, addr, renmei) = l
    c = canvas.Canvas('card' + str(pg) + '.pdf', pagesize=(100 * mm, 148 * mm))
    pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC))
    # Create textobject
    textobject = c.beginText()
#   郵便番号
    textobject.setTextOrigin(45 * mm, 126 * mm)
    textobject.setFont('GenShinGothic', 20)
    textobject.setCharSpace(8.4)
    textobject.textLine(post_code)
#   住所
    textobject.setTextOrigin(30 * mm, 90 * mm)
    textobject.setFont('GenShinGothic', 11)
    textobject.setCharSpace(0)
    textobject.textLine(addr)
#   氏名
    textobject.setTextOrigin(30 * mm, 80 * mm)
    textobject.setCharSpace(4)
    textobject.textLine(sei + ' ' + mei + ' 様')
    if renmei:
        textobject.textLine(sei + ' ' + renmei + ' 様')

    c.drawText(textobject)
    c.save()

if __name__ == '__main__':
    adrL1 = ['服部', '半蔵', '1111111', '大江戸区城内西1-1','']
    adrL2 = ['平', '将門','2222222', '大江戸区城内東2-2', '御前']
    adrL = [ adrL1, adrL2 ]
    count_pg = 1
    for l in adrL:
        mk1PDF(count_pg,l)
        count_pg += 1
