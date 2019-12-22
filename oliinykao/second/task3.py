"""
Вивести даний текст по одному слову, щоб остання літера була у верхньому регістрі
"""
mytext = "London is the capitol of Great Britain"
mylist = mytext.split(' ')
for word in mylist:
    print(word[:len(word)-1] + word[len(word) - 1].upper())