"""
Вивести даний текст по одному слову, щоб остання літера була у верхньому регістрі
"""
mytext = "London is the capitol of Great Britain"
def last_letter_upper(string):
    list_of_words = re.split("[ .,!?:;-]", string)
    for word in list_of_words:
        print(word[:len(word)-1] + word[len(word) - 1].upper())
last_letter_upper(mytext)
