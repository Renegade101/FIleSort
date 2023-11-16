from tkinter import *
import os, shutil



window = Tk()
window.geometry('600x150')
window.title('FileSort')
window.wm_attributes('-topmost', 1)

l1 = Label(window, text='Выберите директорию:')
l1.grid(row=0, column=0, sticky=W, pady=2)

l2 = Label(window, text="")
l2.grid(row=3, column=1, sticky=W, pady=2)

Edirpath = Entry(window, width=50)
Edirpath.grid(row=0, column=1, pady=2)

def Show_res():
    l2['text'] = ('Файлы в директории ',Edirpath.get(), 'отсортированы')
def Sort():
    dirpath = Edirpath.get()
    filename = os.listdir(dirpath)
    foldernames = ['Text', 'Data', 'Images', 'Other']

    for loop in range(0, 4):
        if not os.path.exists(dirpath + foldernames[loop]):
            os.makedirs(dirpath + foldernames[loop])

    for file in filename:
        if '.csv' in file and not os.path.exists(dirpath + 'Data/' + file):
            shutil.move(dirpath + file, dirpath + 'Data/' + file)
        elif '.png' in file and not os.path.exists(dirpath + 'Images/' + file):
            shutil.move(dirpath + file, dirpath + 'Images/' + file)
        elif '.txt' in file and not os.path.exists(dirpath + 'Text/' + file):
            shutil.move(dirpath + file, dirpath + 'Text/' + file)
        elif file:
            shutil.move(dirpath + file, dirpath + 'Other/' + file)



b1 = Button(window, text = "Выбрать", command=lambda:[Sort(), Show_res()])
b1.grid(row = 0, column = 2, sticky =E)


window.mainloop()