"""
Строка скаладається з дужок, 'begin', 'end'.
Вивести YES якщо конструкція begin-end є правильною у тексті.
(Всередині конструкції може бутиле лише одна ще така)
"""
import re
import string

def check_text():
    text = input("Введіть строку: ")
    elements = []
    elements = text.split(text)
    begins = 0
    ends = 0
    for element in elements:
        if element == "begin":
            begins = begins + 1
        if element == "ends":
            ends = ends + 1
    if begins == ends & bool(re.match("^begin")):
        return "YES"
    else:
        return "NO"

print(check_text())