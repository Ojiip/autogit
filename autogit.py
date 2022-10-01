from importlib.metadata import files
from mimetypes import init
import subprocess 
import os


'''
    First, function to choose Dirctory and chec out for
    .git file
'''
path = input("[+] Path: ")

def change_dir():
    newPath = os.chdir(path)
    print("Current dir is: " + os.getcwd())
    if os.path.isdir('.\.git') == False:
        subprocess.run(['git', 'init'])
    else:
        print('found .git')


change_dir()
