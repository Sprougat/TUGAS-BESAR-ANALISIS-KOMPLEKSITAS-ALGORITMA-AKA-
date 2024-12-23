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
Sorting adalah proses mengatur elemen-elemen dalam suatu koleksi (seperti array atau list) berdasarkan kriteria tertentu, seperti nilai yang meningkat (ascending) atau menurun (descending). Sorting mempermudah proses pencarian, analisis, dan manipulasi data.

 Merge Sort

Merge Sort adalah algoritma pengurutan berbasis divide and conquer. Algoritma ini membagi array menjadi sub-array lebih kecil hingga ukuran satu elemen, kemudian menggabungkannya kembali dalam urutan yang benar. Merge Sort memiliki dua varian utama:

- Iteratif: Menggunakan pendekatan berbasis iterasi dengan loop untuk melakukan penggabungan data.

- Rekursif: Menggunakan pemanggilan fungsi secara rekursif untuk membagi dan menggabungkan data.

---

## 2. Deskripsi Program
Program ini membandingkan kinerja Merge Sort Iteratif untuk pengurutan secara ascending dan descending berdasarkan harga dan Merge Sort Rekursif untuk pengurutan secara ascending dan descending berdasarkan rating. Pengguna dapat memasukkan data produk berupa nama, harga, dan rating. Program mencetak hasil pengurutan beserta waktu eksekusi untuk setiap metode.

Program ini mengimplementasikan dua varian Merge Sort (Iteratif dan Rekursif) untuk mengurutkan data produk berdasarkan dua kriteria:

- Harga produk secara ascending menggunakan Merge Sort Iteratif.

- Harga produk secara descending menggunakan Merge Sort Rekursif.

- Rating produk secara ascending menggunakan Merge Sort Iteratif.

- Rating produk secara descending menggunakan Merge Sort Rekursif.

---

## 3. Algoritma yang Digunakan

### Merge Sort Iteratif
Algoritma ini menggunakan pendekatan iteratif dengan loop untuk membagi array menjadi bagian kecil, kemudian menggabungkannya kembali dalam ukuran yang semakin besar. Proses ini diulang hingga seluruh array diurutkan.

### Merge Sort Rekursif
Pendekatan rekursif membagi array menjadi dua bagian hingga ukuran terkecil (satu elemen), kemudian menggabungkannya kembali secara rekursif dengan membandingkan elemen-elemen sesuai kriteria pengurutan.

---

## 4. Cara Kerja Algoritma pada Code

 # Harga Produk - Ascending (Merge Sort Iteratif)

- Array dibagi menjadi blok kecil berukuran 1.

- Blok-blok digabungkan menggunakan fungsi merge hingga seluruh array terurut secara ascending.

- Proses ini dilakukan secara iteratif dengan ukuran blok yang meningkat secara eksponensial.

 # Harga Produk - Descending (Merge Sort Rekursif)

- Array dibagi menjadi dua bagian hingga hanya tersisa satu elemen di setiap bagian.

- Bagian-bagian tersebut digabungkan kembali secara rekursif menggunakan fungsi merge dalam urutan descending.

- Proses berakhir ketika seluruh array terurut secara descending.

# Rating Produk - Ascending (Merge Sort Iteratif)

- Prosesnya identik dengan iteratif untuk harga, tetapi kriteria pengurutan didasarkan pada nilai rating.

- Penggabungan dilakukan menggunakan fungsi merge untuk menghasilkan urutan ascending berdasarkan rating.

# Rating Produk - Descending (Merge Sort Rekursif)

- Langkah-langkahnya sama dengan rekursif untuk harga, tetapi kriteria pengurutan adalah rating.

- Hasil akhir berupa array rating yang terurut secara descending.


---

## 5. Output
![image](https://github.com/user-attachments/assets/ba4016ec-402e-4400-9e2a-f6fc25770c86)

![image](https://github.com/user-attachments/assets/2b65362e-68a1-46ff-9714-b408f1625301)

---

## 6. Analisis

![image](https://github.com/user-attachments/assets/dac9e8a4-6e44-4791-a027-7f6571da4958)

### Struktur Algoritma dan Kompleksitas
 # Kompleksitas Waktu

Merge Sort memiliki kompleksitas waktu sebagai berikut:

- Best Case: O(n log n)

- Worst Case: O(n log n)

- Average Case: O(n log n)

Kompleksitas ruang tambahan adalah O(n) karena diperlukan array temporer untuk penggabungan data.

Dalam perbandingan kinerja antara Merge Sort Iteratif dan Merge Sort Rekursif, kedua algoritma memiliki kompleksitas waktu yang sama, yaitu (O(n \log n)), namun kinerja praktisnya dapat bervariasi tergantung pada ukuran dataset. Merge Sort Iteratif cenderung lebih efisien pada dataset besar karena menghindari overhead pemanggilan fungsi yang ada pada Merge Sort Rekursif, yang dapat menyebabkan penurunan kinerja akibat penggunaan stack frame tambahan. Meskipun Merge Sort Rekursif lebih mudah dipahami dan diimplementasikan, terutama untuk dataset kecil, penggunaan memori yang lebih tinggi dan potensi stack overflow pada dataset besar menjadikannya kurang ideal dalam konteks aplikasi nyata. Oleh karena itu, untuk aplikasi yang memerlukan kecepatan dan efisiensi, terutama dalam pengurutan produk di marketplace, Merge Sort Iteratif adalah pilihan yang lebih baik, sedangkan Merge Sort Rekursif lebih sesuai untuk tujuan pendidikan dan pemahaman konsep dasar algoritma.
 
## 7. Kesimpulan
Dalam konteks pengujian yang dilakukan, Merge Sort Rekursif menunjukkan waktu eksekusi yang lebih baik pada dataset kecil. Namun, Merge Sort Iteratif lebih unggul dalam hal efisiensi dan stabilitas pada dataset besar.

  -  Untuk dataset kecil, Merge Sort Rekursif dapat digunakan untuk kemudahan pemahaman dan implementasi.

  -  Untuk dataset besar, Merge Sort Iteratif adalah pilihan yang lebih baik karena efisiensi waktu dan penggunaan memori yang lebih baik.
