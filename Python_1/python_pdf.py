import pyPDF
pdfFileObj=open("questions.pdf",'rb') # I changed the name of original pdf to questions.pdf
pdfReader=pyPDF.pdfFileReader(pdfFileObj)
pdfObj=pdfReader.getPage(0)
print(pdfObj.extractText())