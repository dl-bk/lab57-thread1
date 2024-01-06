import threading
count_even_numbers = 0
count_odd_numbers = 0


file_path = "123.txt"

with open(file_path, "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

def write_even_numbers(numbers, file_name):
    even_numbers = [str(num) + "\n" for num in numbers if not num & 1]
    global count_even_numbers
    count_even_numbers = len(even_numbers)
    with open(file_name, "w") as file:
        file.writelines(even_numbers)
    return len(even_numbers)


def write_odd_numbers(numbers, file_name):
    odd_numbers = [str(num) + "\n" for num in numbers if num & 1]
    global count_odd_numbers
    count_odd_numbers = len(odd_numbers)
    with open(file_name, "w") as file:
        file.writelines(odd_numbers)
    return len(odd_numbers)


even_thread = threading.Thread(target=write_even_numbers, args=(numbers, "even_numbers.txt"))
odd_thread = threading.Thread(target=write_odd_numbers, args=(numbers, "odd_numbers.txt"))

even_thread.start()
odd_thread.start()
even_thread.join()
odd_thread.join()

print("Кількість парних чисел ", count_even_numbers)
print("Кількість непарних чисел ", count_odd_numbers)