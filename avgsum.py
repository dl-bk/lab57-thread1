# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. 
# Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

import threading

def find_sum(arr):
    summ = sum(arr)
    print(summ)
    return summ

def avg(arr):
    avarage = sum(arr) / len(arr)
    print(avarage)
    return avarage

array = [10, 23, 4, 6, 547]

t1 = threading.Thread(target=find_sum, args=(array, ))
t2 = threading.Thread(target=avg, args=(array, ))

t1.start()
t2.start()

t1.join()
t2.join()

