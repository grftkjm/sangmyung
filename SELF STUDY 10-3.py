from tkinter import *

fnameList = ["bear.gif", "bee.gif", "cupid.gif", "dog.gif", "dog2.gif", "sun.gif", "sun2.gif", "tractor.gif", "unicorn.gif"]
num = 0


def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="C:\\Users\\withj\\Desktop\\python실습\\.dist\\windowP\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fnameLabel.configure(text=fnameList[num])  

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:\\Users\\withj\\Desktop\\python실습\\.dist\\windowP\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fnameLabel.configure(text=fnameList[num])  

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="C:\\Users\\withj\\Desktop\\python실습\\.dist\\windowP\\" + fnameList[0])
pLabel = Label(window, image=photo)

fnameLabel = Label(window, text=fnameList[0], font=("Arial", 12))

btnPrev.place(x=250, y=10)
fnameLabel.place(x=320, y=10) 
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()