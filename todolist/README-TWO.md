### Perbedaan antara asynchronous programming dengan synchronous programming.
### Paradigma Event-Driven Programming pada penerapan JavaScript dan AJAX.
### Penerapan asynchronous programming pada AJAX.
### Implementasi
##### Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
- AJAX GET
1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
2. Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
3. Lakukan pengambilan task menggunakan AJAX GET.
- AJAX POST
1. Buatlah sebuah tombol `Add Task` yang membuka sebuah modal dengan form untuk menambahkan task.
2. Buatlah view baru untuk menambahkan task baru ke dalam database.
3. Buatlah path `/todolist/add` yang mengarah ke view yang baru kamu buat.
4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/todolist/add`
5. Tutup modal setelah penambahan task telah berhasil dilakukan.
6. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
