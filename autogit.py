from distutils.cmd import Command
from importlib.metadata import files
from mimetypes import init
import subprocess 
import os


'''

    Local Opration --> phase [1] of the prgrame
    task[1] --> Take user input and search in the folder for .git, 
    if found return the new path, if don't CREATE one by COMMAND git init (TRY TO OPTEMIZE)

    task[2] --> adding to the stage area and ask for user what to include in the staging area (TRY TO OPTEMIZE)

'''
path = input(str("[+] Path: "))                 

def user(current):
    
    newpath = os.chdir(path)
    if os.path.isdir('.\.git') == False: 
        subprocess.run(['git', 'init'])
    else:
        print("./git FOUND")
    return newpath     


def take_action():      
    user_input = input("choose file: ")
    subprocess.run(['git', 'add', user_input])
    subprocess.run(['git', 'status'])

user(path)    
take_action()