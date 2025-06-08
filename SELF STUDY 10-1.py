from tkinter import *
window=Tk()

photo=PhotoImage(file="C:\\Users\\withj\\Desktop\\python실습\\.dist\\windowP\\dog.gif")
photo2=PhotoImage(file="C:\\Users\\withj\\Desktop\\python실습\\.dist\\windowP\\dog2.gif")
label1=Label(window, image=photo)
label2=Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()