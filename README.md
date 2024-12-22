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

# Hasil Perbandingan

Merge Sort Iteratif (Ascending): Memiliki waktu eksekusi lebih lama.
Merge Sort Rekursif (Descending): Lebih cepat dalam pengujian ini.

