import time
import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

def quick_sort_iterative(arr, ascending=True):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        if start < end:
            pivot_index = partition(arr, start, end, ascending)
            stack.append((start, pivot_index - 1))
            stack.append((pivot_index + 1, end))

def partition(arr, start, end, ascending):
    pivot = arr[end].price
    i = start - 1

    for j in range(start, end):
        if (ascending and arr[j].price < pivot) or (not ascending and arr[j].price > pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def merge_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], ascending)
    right = merge_sort(arr[mid:], ascending)

    return merge(left, right, ascending)

def merge(left, right, ascending):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (ascending and left[i].price < right[j].price) or (not ascending and left[i].price > right[j].price):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(sort_function, data, ascending=True, is_recursive=False):
    start_time = time.time()
    if is_recursive:
        sorted_data = sort_function(data, ascending)
    else:
        sort_function(data, ascending)
        sorted_data = data
    duration = time.time() - start_time
    return duration, sorted_data

def input_products():
    products = []
    n = int(input("Masukkan jumlah produk: "))
    for i in range(n):
        print(f"Produk {i + 1}:")
        name = input("  Nama Produk: ")
        price = float(input("  Harga Produk: "))
        rating = float(input("  Rating Produk: "))
        products.append(Product(name, price, rating))
    return products


if __name__ == "__main__":
    print("=== Input Produk ===")
    products = input_products()

    quick_sort_data = products.copy()
    merge_sort_data = products.copy()

    quick_sort_duration, quick_sort_result = measure_time(quick_sort_iterative, quick_sort_data, ascending=True)

    merge_sort_duration, merge_sort_result = measure_time(merge_sort, merge_sort_data, ascending=False, is_recursive=True)

    print("\n=== Hasil Quick Sort (Iteratif, Ascending) ===")
    print(f"Waktu eksekusi: {quick_sort_duration:.6f} detik")
    for product in quick_sort_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    print("\n=== Hasil Merge Sort (Rekursif, Descending) ===")
    print(f"Waktu eksekusi: {merge_sort_duration:.6f} detik")
    for product in merge_sort_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    algorithms = ['Quick Sort (Ascending)', 'Merge Sort (Descending)']
    durations = [quick_sort_duration, merge_sort_duration]

    plt.bar(algorithms, durations, color=['blue', 'orange'])
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Sorting Algorithms Execution Time')
    plt.show()
