from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm

GEN_SHIN_GOTHIC = "./fonts/GenShinGothic-P-Light.ttf"

def textobject_char_spacing():
    c = canvas.Canvas('card.pdf', pagesize=(100 * mm, 148 * mm))
    pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC))
    # Create textobject
    textobject = c.beginText()
    # Set text location (x, y)
    textobject.setTextOrigin(45 * mm, 126 * mm)
    textobject.setFont('GenShinGothic', 20)
    spacing = 8.4 
    textobject.setCharSpace(spacing)
    line = '9999999'
    textobject.textLine(line)
    textobject.setTextOrigin(30 * mm, 90 * mm)
    textobject.setFont('GenShinGothic', 11)
    textobject.setCharSpace(0)
    line = '東京都目黒区洗足1-29-2'
    textobject.textLine(line)
    textobject.setTextOrigin(30 * mm, 80 * mm)
    line = '高野由紀夫'
    textobject.textLine(line)

    c.drawText(textobject)
    c.save()
if __name__ == '__main__':
    textobject_char_spacing()
