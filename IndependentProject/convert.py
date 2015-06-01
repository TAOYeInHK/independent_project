__author__ = 'ty'

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from os import listdir

def convert_pdf_to_txt(path):
    index = 0
    for filename in listdir(path):
        if index == 0 :
            index += 1
        else :

            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            codec = 'utf-8'
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            outputfile = filename+".txt"
            fp = file(path+"/"+filename, 'rb')
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos=set()
            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
                interpreter.process_page(page)
            string = retstr.getvalue()
            with open('/Users/ty/Desktop/text/'+outputfile, 'w') as writer:
                writer.write(string)
            fp.close()
            device.close()
            retstr.close()



convert_pdf_to_txt('/Users/ty/Desktop/allpaper')