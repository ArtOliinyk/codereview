"""
Строка скаладається з дужок, 'begin', 'end'.
Вивести YES якщо конструкція begin-end є правильною у тексті.
(Всередині конструкції може бутиле лише одна ще така)
"""
def check_text():
    text = input("Введіть строку: ")
    begins = 0
    ends = 0
    for element in text:
        if element == "(":
            begins += 1
        if element == ")":
            ends += 1
    if (begins == ends) & (begins != 0) & (ends != 0):
        return "YES"
    else:
        return "NO"

print(check_text())
