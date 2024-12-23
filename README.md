# TUGAS-BESAR-ANALISIS-KOMPLEKSITAS-ALGORITMA-AKA-
## Perbandingan Kinerja Algoritma Merge Sort (Iteratif dan Rekursif) dalam Pengurutan Produk Marketplace

**ANGGOTA KELOMPOK**
- Rafaldo Al Maqdis (2311102099)
- Naufal Geraldo Putra Pramudianartono (2311102154)

Kelas: IF-11-4  
Program Studi Teknik Informatika  
Telkom University Purwokerto  

---

## 1. Dasar Teori
Sorting adalah proses pengurutan elemen data berdasarkan kriteria tertentu, seperti harga atau rating. Sorting mempermudah analisis data dalam aplikasi nyata seperti marketplace, di mana pengguna sering memerlukan pengurutan berdasarkan harga terendah atau rating tertinggi.

**Merge Sort** adalah algoritma sorting berbasis divide-and-conquer yang membagi array menjadi sub-array, mengurutkan setiap sub-array, lalu menggabungkannya kembali. Merge Sort memiliki dua implementasi umum:
- **Iteratif**: Menggunakan loop untuk mengatur proses pembagian dan penggabungan data.
- **Rekursif**: Menggunakan pemanggilan fungsi secara rekursif untuk membagi data hingga tersisa satu elemen, kemudian menggabungkannya kembali secara berurutan.

---

## 2. Deskripsi Program
Program ini membandingkan kinerja Merge Sort Iteratif untuk pengurutan secara ascending berdasarkan harga dan Merge Sort Rekursif untuk pengurutan secara descending berdasarkan rating. Pengguna dapat memasukkan data produk berupa nama, harga, dan rating. Program mencetak hasil pengurutan beserta waktu eksekusi untuk setiap metode.

---

## 3. Algoritma yang Digunakan

### Merge Sort Iteratif
Algoritma ini menggunakan pendekatan iteratif dengan loop untuk membagi array menjadi bagian kecil, kemudian menggabungkannya kembali dalam ukuran yang semakin besar. Proses ini diulang hingga seluruh array diurutkan.

### Merge Sort Rekursif
Pendekatan rekursif membagi array menjadi dua bagian hingga ukuran terkecil (satu elemen), kemudian menggabungkannya kembali secara rekursif dengan membandingkan elemen-elemen sesuai kriteria pengurutan.

---

## 4. Cara Kerja Algoritma pada Code

### Merge Sort Iteratif (Ascending by Price)
1. **Inisialisasi**: Program mempersiapkan array sementara untuk menyimpan elemen selama penggabungan.
2. **Pembagian dan Penggabungan**: Array dibagi menjadi blok berukuran size, yang dimulai dari 1 hingga ukuran array. Blok-blok ini digabungkan menggunakan fungsi merge, yang membandingkan elemen-elemen dari dua sub-array.
3. **Pengulangan**: Ukuran blok bertambah dua kali lipat pada setiap iterasi hingga seluruh array selesai diurutkan.

### Merge Sort Rekursif (Descending by Rating)
1. **Pembagian**: Array dibagi menjadi dua bagian menggunakan rekursi hingga ukuran terkecil (satu elemen).
2. **Penggabungan**: Fungsi rekursif merge_recursive menggabungkan dua sub-array dengan membandingkan elemen-elemen dari kiri dan kanan berdasarkan kriteria pengurutan.
3. **Pengembalian**: Hasil penggabungan dikembalikan ke tingkat rekursi sebelumnya hingga seluruh array selesai diurutkan.

---

## 5. Output
![output](https://github.com/user-attachments/assets/9a4e2599-0482-4017-9ec6-e8e6a481eaf7)

---

## 6. Analisis
![grafik](https://github.com/user-attachments/assets/274f1dcf-6e39-4c7e-90a3-30bbabe040af)

### Struktur Algoritma dan Kompleksitas
- **Merge Sort Iteratif (Ascending)**:
  - Implementasi berbasis looping dengan menggunakan ukuran subarray yang bertambah secara eksponensial (\(size = 1, 2, 4, \dots\)) hingga seluruh array terurut.
  - **Kompleksitas waktu**: \(O(n \log n)\), karena setiap elemen diproses dalam logaritmik jumlah penggabungan subarray.
  - **Kompleksitas ruang**: Lebih rendah dibandingkan versi rekursif, karena hanya memerlukan array sementara (temp) untuk menyimpan hasil penggabungan.

- **Merge Sort Rekursif (Descending)**:
  - Implementasi berbasis pemanggilan fungsi rekursif. Array dibagi dua secara terus-menerus hingga menjadi unit
 
### Kesimpulan
