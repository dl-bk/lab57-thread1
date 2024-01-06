# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

import threading

# file_path = str(input("enter file path: "))

file_path = "text.txt"
# word = input("Word to search: ")
word = "exponent"

with open(file_path, "r") as rfile:
    sentences = [line.strip() for line in rfile.readlines()] 



def find_word(arr):
    res = []
    for sent in sentences:
        if word in sent.lower():
            res.append(sent)

    print(res)

t1 = threading.Thread(target=find_word, args=(sentences, ))

t1.start()
t1.join()