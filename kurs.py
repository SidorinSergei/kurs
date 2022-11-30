import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, NW
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')

def viewImage(image,name):
    cv2.namedWindow(''+name, cv2.WINDOW_NORMAL)
    cv2.imshow(''+name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def select_file():
    color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
                      'white': [[180, 18, 255], [0, 0, 231]],
                      'red1': [[180, 255, 255], [159, 50, 70]],
                      'red2': [[9, 255, 255], [0, 50, 70]],
                      'green': [[89, 255, 255], [36, 50, 70]],
                      'blue': [[128, 255, 255], [90, 50, 70]],
                      'yellow': [[35, 255, 255], [25, 50, 70]],
                      'purple': [[158, 255, 255], [129, 50, 70]],
                      'orange': [[24, 255, 255], [10, 50, 70]],
                      'gray': [[180, 18, 230], [0, 0, 40]]}


    filetypes = (
        ('Photo', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    cl = combobox.get()

    high_,low_ = color_dict_HSV.setdefault(cl)
    print(high_)
    low_= np.array(low_)
    high_= np.array(high_)
    image = cv2.imread(filename)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    viewImage(hsv_img, 'convert_in_HSV')  ## 1


    curr_mask = cv2.inRange(hsv_img, low_, high_)
    hsv_img[curr_mask > 0] = (high_)
    if cl!="black":
        hsv_img[curr_mask == 0] = ([180, 255, 30])
    else:
        hsv_img[curr_mask == 0] = ([89, 255, 255])
    viewImage(hsv_img, 'maska')  ## 2

    ## Преобразование HSV-изображения к оттенкам серого для дальнейшего оконтуривания
    RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
    viewImage(gray, 'gray')  ## 3

    ret, threshold = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#Бинаризация Otsu
    viewImage(threshold, 'finish_maska')  ## 4

    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
    viewImage(image, 'final')  ## 5

# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

colors = ('black', 'white', 'red1', 'red2', 'green', 'blue', 'yellow', 'purple', 'orange', 'gray')

combobox = ttk.Combobox(values=colors)
combobox.pack(anchor=NW, padx=6, pady=6)

open_button.pack(expand=True)

# run the application
root.mainloop()
