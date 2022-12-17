from PyPDF2 import PdfFileReader, PdfFileWriter

#파일명 받기
path = str(input("What is the file name?-ex.test.pdf\n"))

pdfReader = PdfFileReader(path, "rb")

newpdfWriter = PdfFileWriter()

#원하는 페이지 번호
while True:
    pgnum = int(input("Which page do you want to extract?-if finished please type 0\n"))
    if pgnum==0:
        break
    newpdfWriter.addPage(pdfReader.getPage(pgnum))
    print("Added page number  "+str(pgnum)+"\n")
    

#저장 이름 설정
newfile = str(input("Please type the new file name - ex.test\n"))

newpdfWriter.write(open("./"+newfile+".pdf", "wb"))

print("Saved successfully")
