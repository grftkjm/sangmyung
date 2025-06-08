import os

fName, outList, outStr = "", [], ""
outFp = None
outStr = ""

fName = input("파일명을 입력하세요: ")

if os.path.exists(fName):
    outFp=open(fName,"w", encoding="UTF8")
else:    
    print("%s 파일이 없습니다."%fName)

while True:
    outStr=input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break
    
outFp.close()
print("---정상적으로 파일에 씀---")