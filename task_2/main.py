def binary_search(arr, target):
    """
    Виконує двійковий пошук для відсортованого масиву з дробовими числами.

    Параметри:
    arr (list): Відсортований масив чисел.
    target (float): Цільове значення для пошуку.

    Повертає:
    tuple: Кортеж з кількістю ітерацій та верхньою межею (найменший елемент, більший або рівний цільовому значенню).
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2  # Оптимізація обчислення середнього значення
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)

# Приклади використання:
arrays = [
    ([1.1, 2.2, 3.3, 4.4, 5.5], 3.5),
    ([], 3.5),  # Порожній масив
    ([1.1, 2.2, 3.3, 4.4, 5.5], 6.0),  # Ціль більше за всі елементи
    ([1.1, 2.2, 3.3, 4.4, 5.5], 0.5),  # Ціль менше за всі елементи
]

for arr, target in arrays:
    result = binary_search(arr, target)
    print(f"Масив: {arr}, Ціль: {target}, Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
