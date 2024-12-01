from tkinter import *
from tkinter import *
from random import *

def keygen_answer(word, ints):  # word - просто затычка для того, чтобы вывелось красивенько
    # блок миксования чисел (1 и 2 блоки чисел)
    mass =[]
    for nums in str(ints):
        mass.append(int(nums))
    mass1, mass2 = mass[0:3], mass[3:6]
    shuffle(mass1)
    shuffle(mass2)
    chislo1, chislo2 = '', ''
    for frst_num in mass1: chislo1+=str(frst_num)        
    for sec_num in mass2: 
        chislo2+=str(sec_num)

    # 3 блок - сумма 1 и 2 блока чисел 
    sum_frst_sec = str(int(chislo1) + int(chislo2)).zfill(4)
    # sum_frst_sec = нужно сделать это число по умолчанию 4-значн и сложить 1 и 2 блок чисел
    # делается через .zfill(n), n - колво чисел всего в строке

    # блок миксования букв (1 и 2 блоки)
    # 2 рандомные буквы из A-Z через .sample(x,y), x - список/строка, y - колво случ элем
    alph1, alph2 = [], []
    str1,str2 = '',''
    for i in range(ord('A'), ord('A')+26):
        alph1.append(chr(i))
        alph2.append(chr(i))
    for bukovka1 in sample(alph1,2): str1+=bukovka1
    for bukovka2 in sample(alph2,2): str2+=bukovka2

    key = '{}{}-{}{} {}'.format(chislo1, str1, chislo2, str2, sum_frst_sec)
    lbl.configure(text='Ваш ключ: ')
    lb2.configure(text=key)


def on_button_click():
    input_value = txt.get()
    if input_value.isdigit() and len(input_value) == 6:
        keygen_answer('*', input_value)
    else:
        lbl.configure(text="Введите 6-значное число.")


window = Tk()
window.title("Изображения")
window.geometry('640x360')
window.resizable(0,0)


# def img():
#     img = PhotoImage(file="stalker_pic.png")
#     label = Label(window, image=img)
#     label.image_ref = img
#     label.pack()


# img()
greetings = Label(window, text='Введите 6-значное число в 10-СС, пожалуйста')
greetings.grid(column=0,row=0)


txt = Entry(window, width=10)
txt.grid(column=0,row=1)
txt.focus()
# хакнуть систему(осуждаю, иди в стим)
btn = Button(window, text='кнопка запуска', command=on_button_click)
btn.grid(column=1,row=1)


lbl = Label(window, text="Ваш ключ: ")
lbl.grid(column=0,row=2)
lb2 = Label(window, text="")
lb2.grid(column=1,row=2)

window.mainloop()