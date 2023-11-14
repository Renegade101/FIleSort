import os, shutil

dirpath = r'C:/Users/danil/Downloads/'

filename = os.listdir(dirpath)

foldernames = ['Text', 'Data', 'Images', 'Other']

for loop in range(0,4):
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
