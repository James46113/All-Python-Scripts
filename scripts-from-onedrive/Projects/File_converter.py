import ntpath
from tkinter import filedialog, Tk
from docx import Document
import os

root = Tk()
root.withdraw()


def get_text(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


to_copy_file = filedialog.askopenfilename(parent=root, title='Please select a file', filetypes=(("Documents", ".docx .doc"), ("All Files", "*.*")))
if to_copy_file == "":
    exit()
text = get_text(to_copy_file)

file = filedialog.askdirectory(title='Please select a folder')
if file == "":
    exit()
name = file + "/" + os.path.splitext(ntpath.basename(to_copy_file))[0] + ".txt"
new_file = open(name, 'w')

new_file.write(text)
