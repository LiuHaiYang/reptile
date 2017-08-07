#把任意的PDF读成字符串，转换成文件对象
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr,retstr,laparams=laparams)
    process_pdf(rsrcmgr,device,pdfFile)

    content = retstr.getvalue()
    device.close()
    return content
#网页PDF
pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
#本地PDF文件
# pdfFile = open("",'rb')

outputString= readPDF(pdfFile)

print(outputString)
pdfFile.close()