>>>from pathlib import Path
>>> import os

""" OS module commands
os.path.abspath(path) - this command will return a string of the absolute path of a n arguement.
this is an easy way to convert a relative path to an absolute path
>>> os.path.abspath('.')
'C:\\Users\\me'
>>>
#similar
>>> Path.cwd()
WindowsPath('C:/Users/me')

os.path.isabs(path) - will return True if the arguement is an absolute path or 
False if it is a relative Path
>>> os.path.isabs('.')
False
>>>

os.path.relpath(path,start) - will return a string of a relative path from the start path to path. 
If start is not provided, the current working directory is used as the start path

"""
#Findinf File Sizes and Folder Contents
"""
os.path.getsize(path) - will return the size in bytes of the file in the (path) arguement

os.listdir(path) - will return a list of filename strings for each file in the (path) arguement.

dDrive = Path('D:/')
dDrive.exists()
#response False (so you know that the drive is missing or True its where its suppossed to be)

open() - function will return the file object

read() - or write() - 

close() - closes the file object


"""

>>> Path.cwd()
WindowsPath('C:/Users/me')
>>>### chaning directory
os.chrid('C\\Windows\\Sysytems32')
Path.cwd()
#OUtput WindowsPath('C:/Windows/System32')

#Make directories
>>> os.makedirs('C:\\my_Directory_made_with_python\\my_Pthon_made_dir\\Python_stuff')

#Using Path to mkdir() 
"""You can only make one directory at a time with this function"""
>>> Path(r'C:\Users\me\spam').mkdir() # I made the spam folder


#How to check if a file path is the Absolute pat
>>> Path.cwd().is_absolute()
True
>>>

#To ge the abdolute path from a relative PAth type
>>> Path('my/relative/path')
WindowsPath('my/relative/path')
>>> Path.cwd() / Path('my/relative/path')
WindowsPath('C:/Users/me/my/relative/path')
>>>
#or
>>> Path.home() / Path('my/relative/path')
WindowsPath('C:/Users/me/my/relative/path')
>>>


>>> p = Path('spam.txt')
>>> p.write_text('HELLO, World')
12
>>> p.read_text()
'HELLO, World'
>>>

