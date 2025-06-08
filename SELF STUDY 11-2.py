inFp=None
inList, inStr = [], ""
line_num = 1

inFp=open("C:\\Users\\withj\\Desktop\\python실습\\.dist\\FileTest\\data1.txt", "r", encoding="UTF8")


inList = inFp.readlines()
for inStr in inList:
    print("%d. %s" % (line_num, inStr), end = "")
    line_num += 1
inFp.close()