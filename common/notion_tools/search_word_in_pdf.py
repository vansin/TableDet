#! /usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2
import re

from fuzzywuzzy import fuzz

def search_word_in_pdf(file_name='',search_words = ['mmdetection3d', 'mmocr', 'mmdeploy', 'mmrotate', 'mmflow', 'mmgeneration', 'mmediting', 'labelbee', 'mim', 'mmsegmentation', 'mmselfsup', 'mmdetection', 'mmtracking', 'mmpose', 'mmclassification', 'mmcv', 'mmrazor', 'mmhuman3d', 'mmfewshot', 'mmaction2', 'mmskeleton', 'mmfashion', 'mmaction', 'mmstyles']):

    # Open the pdf file
    object = PyPDF2.PdfFileReader(file_name)

    # Get number of pages
    NumPages = object.getNumPages()

    # Enter code here

    max_ratio = 0
    # Extract text and do the search
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()

        # print(type(Text))
        for search_word in search_words:
            max_ratio = max(max_ratio, fuzz.partial_ratio(search_word, Text))

        # print(type(Text))
        # if re.search(search_word,Text):
        #     print("Pattern Found on Page: " + str(i))

    return max_ratio



def search_word_in_pdf2(file_name, search_word):

    from tika import parser # pip install tika

    raw = parser.from_file(file_name)
    print(raw[search_word])

# def search_word_in_pdf3(file_name, search_word):

#     import fitz # install using: pip install PyMuPDF
#     print(file_name)
#     with fitz.open(file_name) as doc:
#         text = ""
#         for page in doc:
#             text += page.get_text()
#             if search_word in text:
#                 print(search_word)
#         # print(text)


# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO

# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'unicode'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = open(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()


#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)


#     text = retstr.getvalue()

#     fp.close()
#     device.close()
#     retstr.close()
#     return text



if __name__ == "__main__":

    pdf_file_path = '/home/elaine/Documents/cvpr2022/1604.06397v2.Improving_Human_Action_Recognition_by_Non_action_Classification.pdf'

    # search_word_in_pdf3(pdf_file_path, 'Classi.cation')
    # text= convert_pdf_to_txt(pdf_file_path)

    # if 'Classification' in text:

    #     print(text)

    print(search_word_in_pdf(pdf_file_path, ['Classification']))


