import time
import matplotlib.pyplot as plt
from tabulate import tabulate

# Struktur untuk menyimpan data produk
class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

# Merge Sort Iteratif

def merge_sort_iterative(arr, by="price", ascending=True):
    n = len(arr)
    temp = [None] * n

    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            merge(arr, temp, left, mid, right, by, ascending)
        size *= 2
    return arr

# Merge Sort Rekursif
def merge_sort_recursive(arr, by="price", ascending=True):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid], by, ascending)
    right = merge_sort_recursive(arr[mid:], by, ascending)
    return merge_recursive(left, right, by, ascending)

# Fungsi Merge untuk Iteratif
def merge(arr, temp, left, mid, right, by, ascending):
    i, j, k = left, mid, left

    while i < mid and j < right:
        if compare(arr[i], arr[j], by, ascending):
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right):
        arr[i] = temp[i]

# Fungsi Merge untuk Rekursif
def merge_recursive(left, right, by, ascending):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j], by, ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Fungsi Perbandingan
def compare(a, b, by, ascending):
    if by == "price":
        if ascending:
            return a.price < b.price
        return a.price > b.price
    elif by == "rating":
        if ascending:
            return a.rating < b.rating
        return a.rating > b.rating
    return False

# Fungsi untuk mengukur waktu eksekusi
def measure_time(sort_function, data, by="price", ascending=True, is_recursive=False):
    start_time = time.time()
    if is_recursive:
        sorted_data = sort_function(data, by, ascending)
    else:
        sorted_data = sort_function(data, by, ascending)
    duration = time.time() - start_time
    return duration, sorted_data

# Fungsi untuk input data produk dari pengguna
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

# Fungsi utama
if __name__ == "__main__":
    # Input data produk dari pengguna
    print("=== Input Produk ===")
    products = input_products()

    # Duplikasi data untuk pengujian
    data_iterative_price = products.copy()
    data_recursive_price = products.copy()
    data_iterative_rating = products.copy()
    data_recursive_rating = products.copy()

    # Mengukur waktu eksekusi Merge Sort Iteratif (Ascending, Harga)
    iterative_price_duration, iterative_price_result = measure_time(
        merge_sort_iterative, data_iterative_price, by="price", ascending=True, is_recursive=False
    )

    # Mengukur waktu eksekusi Merge Sort Rekursif (Descending, Harga)
    recursive_price_duration, recursive_price_result = measure_time(
        merge_sort_recursive, data_recursive_price, by="price", ascending=False, is_recursive=True
    )

    # Mengukur waktu eksekusi Merge Sort Iteratif (Ascending, Rating)
    iterative_rating_duration, iterative_rating_result = measure_time(
        merge_sort_iterative, data_iterative_rating, by="rating", ascending=True, is_recursive=False
    )

    # Mengukur waktu eksekusi Merge Sort Rekursif (Descending, Rating)
    recursive_rating_duration, recursive_rating_result = measure_time(
        merge_sort_recursive, data_recursive_rating, by="rating", ascending=False, is_recursive=True
    )

    # Menampilkan hasil untuk Harga
    print("\n=== Hasil Merge Sort Iteratif (Ascending, Harga) ===")
    print(f"Waktu eksekusi: {iterative_price_duration:.6f} detik")
    for product in iterative_price_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    print("\n=== Hasil Merge Sort Rekursif (Descending, Harga) ===")
    print(f"Waktu eksekusi: {recursive_price_duration:.6f} detik")
    for product in recursive_price_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    # Menampilkan hasil untuk Rating
    print("\n=== Hasil Merge Sort Iteratif (Ascending, Rating) ===")
    print(f"Waktu eksekusi: {iterative_rating_duration:.6f} detik")
    for product in iterative_rating_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    print("\n=== Hasil Merge Sort Rekursif (Descending, Rating) ===")
    print(f"Waktu eksekusi: {recursive_rating_duration:.6f} detik")
    for product in recursive_rating_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    # Menampilkan perbandingan waktu eksekusi dalam bentuk tabel
    table_data = [
        ["Merge Sort Iteratif (Ascending, Harga)", f"{iterative_price_duration:.6f} detik"],
        ["Merge Sort Rekursif (Descending, Harga)", f"{recursive_price_duration:.6f} detik"],
        ["Merge Sort Iteratif (Ascending, Rating)", f"{iterative_rating_duration:.6f} detik"],
        ["Merge Sort Rekursif (Descending, Rating)", f"{recursive_rating_duration:.6f} detik"],
    ]
    print("\n=== Perbandingan Waktu Eksekusi ===")
    print(tabulate(table_data, headers=["Algoritma", "Waktu Eksekusi"], tablefmt="grid"))

    # Menampilkan grafik perbandingan waktu eksekusi
    algorithms = [
        "Iteratif Ascending (Harga)",
        "Rekursif Descending (Harga)",
        "Iteratif Ascending (Rating)",
        "Rekursif Descending (Rating)"
    ]
    durations = [
        iterative_price_duration,
        recursive_price_duration,
        iterative_rating_duration,
        recursive_rating_duration
    ]

    plt.bar(algorithms, durations, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Sorting Algorithms Execution Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
