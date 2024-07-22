from timeit import timeit
from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search

# Функція для xитання файлів
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Функція для вимірювання часу виконання кожного алгоритму
def compare_algorithms(article1, article2, existing_substring, non_existing_substring):
    # Ініціалізація списку алгоритмів
    algorithms = [
        ("KMP", kmp_search),
        ("Boyer-Moore", boyer_moore_search),
        ("Rabin-Karp", rabin_karp_search)
    ]
    
    # Cписок для збереження результатів вимірювань часу виконання алгоритмів
    results = []
    
    # Цикл для вимірювання часу виконання
    for name, algorithm in algorithms:
        for article, text in [("Article 1", article1), ("Article 2", article2)]:
            for substring in [existing_substring, non_existing_substring]:
                time_taken = timeit(lambda: algorithm(text, substring), number=10)
                results.append((article, name, substring, time_taken))
    
    return results

# Функція для виведення результатів, форматує результати у вигляді таблиці
def print_results(results):
    header = "| Стаття     | Алгоритм        | Підрядок             | Час (секунди) |\n"
    header += "|------------|-----------------|----------------------|---------------|\n"
    rows = [
        f"| {article:10} | {name:15} | {substring:20} | {time_taken:13.6f} |"
        for article, name, substring, time_taken in results
    ]
    return header + "\n".join(rows)


if __name__ == "__main__":
# Читаємо файли
    article1 = read_file('article1.txt')
    article2 = read_file('article2.txt')

# Підрядки для пошуку
    existing_substring = "Література"
    non_existing_substring = "адронний колайдер"

# Порівнюємо алгоритми
    results = compare_algorithms(article1, article2, existing_substring, non_existing_substring)

# Виводимо результати
    output = print_results(results)
    print(output)
