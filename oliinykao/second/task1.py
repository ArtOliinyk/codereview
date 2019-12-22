"""
Вивести всі списки, що існуюють у головному списку
"""
mylist = [True, 2, 'word', [0,2,False], 5, [0,True]]
for element in mylist:
    if isinstance(element, list):
        print(element)