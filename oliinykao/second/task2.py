"""
Вивести суму цифр, що знаходяться у тексті
"""
mytext = "Ашщщівалті6б3б4"
sum = 0
for element in mytext:
    if element in '0123456789':
        sum = sum + int(element)
print(sum)