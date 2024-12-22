# TUGAS-BESAR-ANALISIS-KOMPLEKSITAS-ALGORITMA-AKA-
Perbandingan Kinerja Algoritma Merge Sort (Iteratif dan Rekursif) dalam Pengurutan Produk Marketplace

**ANGGOTA KELOMPOK**
- Rafaldo Al Maqdis (2311102099)
- Naufal Geraldo Putra Pramudianartono (2311102154)

Kelas: IF-11-4
Program Studi Teknik Informatika
Telkom University Purwokerto

# Dasar Teori
Sorting adalah proses pengurutan elemen data berdasarkan kriteria tertentu, seperti harga atau rating. Sorting mempermudah analisis data dalam aplikasi nyata seperti marketplace, di mana pengguna sering memerlukan pengurutan berdasarkan harga terendah atau rating tertinggi.
Merge Sort adalah algoritma sorting berbasis divide-and-conquer yang membagi array menjadi sub-array, mengurutkan setiap sub-array, lalu menggabungkannya kembali. Merge Sort memiliki dua implementasi umum:

Iteratif: Menggunakan loop untuk mengatur proses pembagian dan penggabungan data.
Rekursif: Menggunakan pemanggilan fungsi secara rekursif untuk membagi data hingga tersisa satu elemen, kemudian menggabungkannya kembali secara berurutan.

# Deskripsi Program
Program ini membandingkan kinerja Merge Sort Iteratif untuk pengurutan secara ascending berdasarkan harga dan Merge Sort Rekursif untuk pengurutan secara descending berdasarkan rating. Pengguna dapat memasukkan data produk berupa nama, harga, dan rating. Program mencetak hasil pengurutan beserta waktu eksekusi untuk setiap metode.

# Algoritma yang Digunakan

  Merge Sort Iteratif

Algoritma ini menggunakan pendekatan iteratif dengan loop untuk membagi array menjadi bagian kecil, kemudian menggabungkannya kembali dalam ukuran yang semakin besar. Proses ini diulang hingga seluruh array diurutkan.

  Merge Sort Rekursif

Pendekatan rekursif membagi array menjadi dua bagian hingga ukuran terkecil (satu elemen), kemudian menggabungkannya kembali secara rekursif dengan membandingkan elemen-elemen sesuai kriteria pengurutan.

# Cara Kerja Algoritma pada Code

        Merge Sort Iteratif (Ascending by Price)

-Inisialisasi: Program mempersiapkan array sementara untuk menyimpan elemen selama penggabungan.
-Pembagian dan Penggabungan: Array dibagi menjadi blok berukuran size, yang dimulai dari 1 hingga ukuran array. Blok-blok ini digabungkan menggunakan fungsi merge, yang membandingkan elemen-elemen dari dua sub-array.
-Pengulangan: Ukuran blok bertambah dua kali lipat pada setiap iterasi hingga seluruh array selesai diurutkan.

        Merge Sort Rekursif (Descending by Rating)

-Pembagian: Array dibagi menjadi dua bagian menggunakan rekursi hingga ukuran terkecil (satu elemen).
-Penggabungan: Fungsi rekursif merge_recursive menggabungkan dua sub-array dengan membandingkan elemen-elemen dari kiri dan kanan berdasarkan kriteria pengurutan.
-Pengembalian: Hasil penggabungan dikembalikan ke tingkat rekursi sebelumnya hingga seluruh array selesai diurutkan.

Source code

import time
import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

def merge_sort_iterative(arr, by="price"):
    n = len(arr)
    temp = [None] * n

    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            merge(arr, temp, left, mid, right, by, ascending=True)
        size *= 2
    return arr

def merge_sort_recursive(arr, by="price"):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid], by)
    right = merge_sort_recursive(arr[mid:], by)
    return merge_recursive(left, right, by, ascending=False)

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

def measure_time(sort_function, data, by="price", is_recursive=False):
    start_time = time.time()
    if is_recursive:
        sorted_data = sort_function(data, by)
    else:
        sorted_data = sort_function(data, by)
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

    iterative_data = products.copy()
    recursive_data = products.copy()

    iterative_duration, iterative_result = measure_time(merge_sort_iterative, iterative_data, by="price", is_recursive=False)

    recursive_duration, recursive_result = measure_time(merge_sort_recursive, recursive_data, by="rating", is_recursive=True)

    print("\n=== Hasil Merge Sort Iteratif (Ascending, Harga) ===")
    print(f"Waktu eksekusi: {iterative_duration:.6f} detik")
    for product in iterative_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    print("\n=== Hasil Merge Sort Rekursif (Descending, Rating) ===")
    print(f"Waktu eksekusi: {recursive_duration:.6f} detik")
    for product in recursive_result:
        print(f"{product.name}: {product.price}, Rating: {product.rating}")

    algorithms = ['Merge Sort Iterative (Ascending)', 'Merge Sort Recursive (Descending)']
    durations = [iterative_duration, recursive_duration]

    plt.bar(algorithms, durations, color=['blue', 'orange'])
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Sorting Algorithms Execution Time')
    plt.show()


# Output
![output](https://github.com/user-attachments/assets/9a4e2599-0482-4017-9ec6-e8e6a481eaf7)

# Analisis
![grafik](https://github.com/user-attachments/assets/274f1dcf-6e39-4c7e-90a3-30bbabe040af)

# Hasil Perbandingan

Merge Sort Iteratif (Ascending): Memiliki waktu eksekusi lebih lama.
Merge Sort Rekursif (Descending): Lebih cepat dalam pengujian ini.



