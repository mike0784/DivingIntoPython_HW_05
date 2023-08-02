import os.path
def parsing(text):
    ss = os.path.split(text)
    return tuple([ss[0]] + ss[1].split("."))

text = "C:\\User\\mike\\GB\\text.txt"
print(parsing(text))