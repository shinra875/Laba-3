from tkinter import *
from tkinter import PhotoImage
from random import shuffle, sample
import pygame


# Music funcs
pygame.mixer.init()

def play():
    pygame.mixer.music.load("8-bit Unity.mp3")
    pygame.mixer.music.play(loops=0)
    

def stop():
    pygame.mixer.music.stop()

# keygen funcs
def keygen_answer(ints):
    mass = []
    for nums in str(ints):
        mass.append(int(nums))
    mass1, mass2 = mass[0:3], mass[3:6]
    shuffle(mass1)
    shuffle(mass2)
    chislo1, chislo2 = '', ''
    for frst_num in mass1: chislo1 += str(frst_num)
    for sec_num in mass2: chislo2 += str(sec_num)

    sum_frst_sec = str(int(chislo1) + int(chislo2)).zfill(4)

    alph1, alph2 = [], []
    str1, str2 = '', ''
    for i in range(ord('A'), ord('A') + 26):
        alph1.append(chr(i))
        alph2.append(chr(i))
    for bukovka1 in sample(alph1, 2): str1 += bukovka1
    for bukovka2 in sample(alph2, 2): str2 += bukovka2

    key = '{}{}-{}{} {}'.format(chislo1, str1, chislo2, str2, sum_frst_sec)
    your_key.configure(text='Ваш ключ: ')
    key_area.configure(text=key)

def on_button_click():
    input_value = txt.get()
    if input_value.isdigit() and len(input_value) == 6:
        keygen_answer(input_value)
    else:
        your_key.configure(text="Введите 6-значное число.")

# Animation func
def moveBall():
    # передвигаем наш овал на 10 пикселей по обеим осям
    canvas.move(my_favorite_oval, 10, 10)
    # повторяем через 200 мс (2 секунда)
    canvas.after(200, moveBall)

# Создаем главное окно
window = Tk()
window.title("Изображения")
window.resizable(0, 0)

# Загружаем изображение в title
img = PhotoImage(file='radiation.png')
window.iconphoto(False, img)
window.title("S.T.A.L.K.E.R 2 keygen")

# Создаем Canvas для фона
canvas = Canvas(window, width=640, height=360)
canvas.pack()

# Загружаем изображение
background_image = PhotoImage(file="stalker_pic.png")
canvas.create_image(0, 0, anchor=NW, image=background_image)

# Размещаем виджеты на Canvas
# 1 line
greetings = Label(window, text='Введите 6-значное число в 10-СС, пожалуйста', bg='white')
canvas.create_window(320, 200, window=greetings)  # Центрируем по x

meteor = Label(window, text='это типа метеор падает, из-за него сталкер 2 не выйдет(прога из прошлого)', bg='white')
canvas.create_window(320, 240, window=meteor)  # Центрируем по x

# 2 line
txt = Entry(window, width=10)
canvas.create_window(200, 280, window=txt)  # Центрируем по x
txt.focus()

btn = Button(window, text='Кнопка запуска', command=on_button_click)
canvas.create_window(420, 280, window=btn)  # Сместим влево

# 3 line
your_key = Label(window, text="Ваш ключ: ", bg='white')
canvas.create_window(200, 320, window=your_key)  # Сместим вправо

key_area = Label(window, text="", bg='white')
canvas.create_window(420, 320, window=key_area)  # Сместим вправо под your_key

# music buttons (0 line)
play_btn = Button(window, text='Play song', command=play)
play_btn.pack(pady=20)
canvas.create_window(200, 30, window=play_btn)  # Сместим вверхнюю часть экрана (левее)

stop_btn = Button(window, text='Stop', command=stop)
stop_btn.pack(pady=20)
canvas.create_window(420, 30, window=stop_btn)  # Сместим вверхнюю часть экрана (правее)

# Анимация
# c = Canvas(window, width=320, height=320, bg='blue')
# c.pack()

# сохраняем номер соданной фигуры в переменную
my_favorite_oval = canvas.create_oval(0, 0, 50, 50, fill='orange')

# спустя 2 секунду (200 мс) после запуска выполнить moveBall
canvas.after(200, moveBall)

window.mainloop()