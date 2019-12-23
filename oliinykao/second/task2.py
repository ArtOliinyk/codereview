"""
Вивести суму цифр, що знаходяться у тексті
"""
def sum_in_string(string):
    sum = 0
    for element in string:
        if element in "0123456789":
            sum += int(element)
