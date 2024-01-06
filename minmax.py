# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. 
# Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран. 

import threading

def find_min(arr):
    print(min(arr))

def find_max(arr):
    print(max(arr))

array = [10, 23, 4, 6, 547]

t1 = threading.Thread(target=find_min, args=(array, ))
t2 = threading.Thread(target=find_max, args=(array, ))

t1.start()
t2.start()

t1.join()
t2.join()
