import os
import sys
from utils import colors

def setIcon(file_extension):
    fExtensions = [
        ('.py', ''),
        ('.lnk', ''),
        ('.webp', '󰋩'),
        ('.pdf', ''),
        ('.docx', '󰈙'),
        ('.pptx', '󱎐'),
        ('.xlsx', '󱎏'),
        ('.jpg', '󰋩'),
        ('.png', '󰋩'),
        ('.mp3', '󰎄'),
        ('.wav', '󱑽'),
        ('.java', ''),
        ('.go', ''),
        ('.js', ''),
        ('.json', '󰘦'),
        ('.jsx', ''),
        ('.css', ''),
        ('.html', ''),
        ('.txt', ''),
        ('.md', ''),
        ('.c', ''),
        ('.cpp', ''),
        ('.h', ''),
        ('.hpp', ''),
        ('.exe', '󰏚'),
        ('.dll', '󰏚'),
        ('.msi', '󰏚'),
        ('.bat', '󰏚'),
        ('.sh', ''),
        ('.pyc', ''),
        ('.pyd', ''),
        ('.pyo', ''),
        ('.pyw', ''),
        ('.pyz', ''),
        ('.key', '󰏚'),
    ]
    
    for ext, icon in fExtensions:
        if ext.lower() == file_extension.lower():
            return icon

def list_directory():
    directory_content = os.listdir(path=os.getcwd())[::-1]
    for content in directory_content:
        file_name, file_extension = os.path.splitext(os.path.join(os.getcwd() + content))
        if os.path.isdir(f"{os.getcwd()}/{content}"):
            print(colors.LIGHTBLUE_EX + content + colors.RESET)
        else:
            print(f"{content} {setIcon(file_extension)}")
    return 0

def list_all_directory():
    if sys.platform == "darwin" or sys.platform == "linux":
        os.system('ls -la')
        return 0
    else:
        os.system('dir')
        return 0