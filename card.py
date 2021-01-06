#
#
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm
#pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
GEN_SHIN_GOTHIC = "./fonts/GenShinGothic-P-Light.ttf"
c = canvas.Canvas('card.pdf', pagesize=(100 * mm, 148 * mm))
pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC))

c.setFont('GenShinGothic', 20)
c.drawString(45 * mm, 125 * mm, '9999999')
c.setFont('GenShinGothic', 12)
c.drawString(30 * mm, 100 * mm, '東京都目黒区洗足1-29-2')
c.drawString(30 * mm, 90 * mm, '高野由紀夫')

c.showPage()
c.save()

