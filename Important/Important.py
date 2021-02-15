from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys, fileinput
from tkinter.messagebox import *

def funktion(a):
    tabs.select(a)


def open_():
    file = askopenfilename()
    for text in fileinput.input(file):
        box.insert(0.0,text)

def save_():
    try:
        file = asksaveasfile(
            mode="w",defaultextension=((".txt"),(".docx")),
            filetypes=(("Notepad",".txt"),("Word",".docx")))
        t=box.get(0.0,END)
        file.write(t)
        file.close()
    except NameError:
        pass

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        main.destroy()
    else:
        showinfo("No")

def imgChange(name):
    global img
    tabs.select(0)
    img=PhotoImage(file=name).subsample(1)
    can.create_image(10,10,image=img,anchor=NW)

def receiptsChange(name):
    global img
    tabs.select(0)
    img=PhotoImage(file=name).subsample(1)
    can.create_image(10,10,image=img,anchor=NW)


gui = Tk()
gui.geometry("900x800")
gui.title("Receipts")

tabs = ttk.Notebook(gui)
text=[1,2,3,4]
tabs1 = Frame(tabs) #рамка-Frame
#tabs2 = Frame(tabs)
#tabs3 = Frame(tabs)
#tabs4 = Frame(tabs)
tabs.add(tabs1,text=1)
#tabs.add(tabs2,text=2)
#tabs.add(tabs3,text=3)
#tabs.add(tabs4,text=4)
tabs.grid(row=0, column=5)

#иконка
icon=["iconfinder_ic_import_contacts_48px_3669166.ico"]
gui.iconbitmap(icon)

 
M = Menu(gui)
gui.config(menu=M)
menu = Menu(M,tearoff=0)
M.add_cascade(label="Menu",menu=menu)
#menu.add_command(label="Tab1",command=lambda:funktion(0))
#menu.add_command(label="Pictures",command=lambda:funktion(1))
#menu.add_command(label="Tab3",command=lambda:funktion(2))
#menu.add_command(label="Tab4",command=lambda:funktion(3))
menu.add_separator()


color = Menu(M,tearoff=1)
M.add_cascade(label="Colors",menu=color)
color.add_command(label="lemonchiffon",command=lambda:gui.config(bg="lemonchiffon"))
color.add_command(label="coral",command=lambda:gui.config(bg="coral"))
color.add_command(label="mediumpurple",command=lambda:gui.config(bg="mediumpurple"))
color.add_command(label="thistle",command=lambda:gui.config(bg="thistle"))
color.add_command(label="maroon",command=lambda:gui.config(bg="maroon"))
color.add_separator()

can=Canvas(tabs1,width=600,height=600)
can.pack()

tmenu = Menu(M,tearoff=2)
M.add_cascade(label="Desserts",menu=tmenu)
tmenu.add_command(label="jam dessert",command=lambda:imgChange("jam dessert.png"))
tmenu.add_command(label="panna cotta",command=lambda:imgChange("Panna Cotta.png"))
tmenu.add_command(label="maskarpone",command=lambda:imgChange("maskarpone.png"))
tmenu.add_command(label="moti",command=lambda:imgChange("moti.png"))
tmenu.add_command(label="cookies",command=lambda:imgChange("Cookies.png"))
tmenu.add_command(label="pavlova",command=lambda:imgChange("Pavlova.png"))

tmenu.add_separator()

rmenu = Menu(M,tearoff=1)
M.add_cascade(label="Desserts Receipts",menu=rmenu)
rmenu.add_command(label="jam dessert",command=lambda:receiptsChange("rjamdessert.png"))
rmenu.add_command(label="panna cotta",command=lambda:receiptsChange("rPannaCotta.png"))
rmenu.add_command(label="maskarpone",command=lambda:receiptsChange("rmaskarpone.png"))
rmenu.add_command(label="moti",command=lambda:receiptsChange("rmoti.png"))
rmenu.add_command(label="cookies",command=lambda:receiptsChange("rCookies.png"))
rmenu.add_command(label="pavlova",command=lambda:receiptsChange("rPavlova.png"))

rmenu.add_separator()



#calculator
expression = "" # объявлена переменная

def press(num):  # Функция для обновления переменной в текстовом поле
    global expression # указывает глобальную переменную expression
    expression = expression + str(num) # склеивание строки
    equation.set(expression) # обновить выражение с помощью метода set
 
 

def equalpress(): # Функция для оценки финальной переменной expression
    try:  # Используется оператор try и except для обработки ошибок типа нуля, ошибка деления и т. д.
        global expression
        total = str(eval(expression)) # функция eval вычисляет выражение и функция str преобразуют результат в строку
        equation.set(total)
        expression = "" # инициализируем (подготавлеваем к работе) переменную expression строкой
    except:
        equation.set(" error ")
        expression = ""


# Функция для очистки содержимого поля ввода текста
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
if __name__ == "__main__":  
 
    equation = StringVar() # StringVar (для изменения текста, этот компонент позволяет создать привязку к строке) - это класс переменной, создаем экземпляр этого класса
    expression_field = Entry(gui, textvariable=equation) # создаем текстовое поле для ввода, показ выражения
    expression_field.grid(columnspan=4, ipadx=70)
 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)



 
    gui.mainloop() 


