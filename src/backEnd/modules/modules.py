import os
import tkinter as tk
from tkinter import filedialog


def choose_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    directory = directory.replace('/','\\')
    print(f'directory: {directory}')

    return directory

def create_project(directory: str, folders: list):
    
    for folder in folders:
        try:
            if '.' in folder:
                with open(os.path.join(directory, folder), 'w') as arquivo:
                    arquivo.write('')
            else:
                print(os.path.join(directory, folder))
                os.makedirs(os.path.join(directory, folder))
        except Exception as error:
            print('Error:', error)

directory = choose_directory()
folders = ['src\\backend\\funcs', 'src\\frontend\\scripts', '.env', '.gitignore']
create_project(directory=directory, folders=folders)
