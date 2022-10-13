### Perbedaan antara _asynchronous programming_ dengan _synchronous programming_
- _Asynchronous programming_ <br>
_Asynchronous programming_ adalah suatu pendekatan pemrograman yang tidak terikat pada input output (I/O) protocol, model ini sangat aplikatif untuk _networking_ dan komunikasi. Model ini menerapkan arsitektur yang _non-blocking_, artinya program tidak akan memblokir eksekusi selanjutnya ketika ada operasi yang sedang berlangsung. Dengan kata lain, _asynchronous programming_ memungkinkan pengeksekusian operasi secara bersamaan tanpa harus menunggu suatu operasi lain untuk selesai. Operasi atau program dapat dieksekusi secara paralel sehingga _throughput_-nya tinggi. Oleh karena itu, _asynchronous programming_ dapat mengirimkan beberapa _requests_ kepada server di saat yang sama. <br>
_Asynchronous programming_ meningkatkan pengalaman pengguna dengan cara mengurangi jeda waktu antara ketika suatu fungsi dijalankan dan ketika nilainya dikembalikan. Pendekatan pemrograman ini relatif lebih kompleks dan lebih baik digunakan untuk program-program penting yang independen.

- _Synchronous programming_ <br>
_Synchronous programming_ adalah suatu model yang menerapkan arsitektur _blocking_. Pendekatan pemrograman ini akan mengikuti alur eksekusi sesuai urutan dan prioritas. Artinya, setiap operasi dijalankan satu per satu. Ketika ada satu operasi yang sedang dijalankan, operasi lainnya diblokir untuk dijalankan. Penyelesaian satu operasi, yaitu ketika nilainya sudah dikembalikan, akan men-_trigger_ operasi selanjutnya. Eksekusi setiap operasi bergantung pada penyelesaian operasi sebelumnya. _Synchronous programming_ hanya bisa mengirimkan satu request kepada server di satu waktu dan akan menunggu nilainya dikembalikan dari server. <br>
Pendekatan ini memang lebih lambat, tapi lebih menguntungkan bagi para pengembang karena lebih mudah diterapkan. Penggunaannya tersedia untuk banyak bahasa pemrograman, kodenya juga akan lebih mudah ditulis dan dimengerti.

### Paradigma _Event-Driven Programming_ pada penerapan JavaScript dan AJAX
_Event-driven programming_ berarti program yang dapat merespon aksi pengguna seperti klik _button_ dan _key presses_. Setiap bentuk interaksi bisa dianggap sebagai _event_. Penerapannya menggunakan suatu _event listener_. Istilahnya, sebagai penangkap _event_ yang mungkin terjadi. _Event listener_ akan menunggu untuk suatu _event_ terjadi. Setelah _event_ ditangkap, _event listener_ akan memanggil kode, yaitu _event handler_, untuk dieksekusi sebagai bentuk _callback_.

### Penerapan _asynchronous programming_ pada AJAX
Dengan AJAX, pertukaran data dengan server dilakukan di belakang layar sehingga memungkinkan halaman web untuk melakukan update secara asinkronus. Konten dari suatu halaman web dapat segera diperbarui berdasarkan tindakan pengguna, seperti klik atau gerakan lainnya. Dengan kata lain, bagian dari suatu halaman web dapat di-_update_ tanpa harus menunggu hasil _reload_ atau refresh untuk seluruh halaman. AJAX juga bisa mengakses data dari sumber eksternal setelah halaman web termuat sepenuhnya. <br>
Karena AJAX tidak bergantung pada server, lingkungannya lebih ke arah _data-driven_ daripada _page-driven_. Inilah yang membuatnya bisa mengeksekusi operasi secara asinkronus dan kapan saja. Secara singkat, setelah user menekan tombol submit, JavaScript akan membuat request kepada server, mengartikan hasilnya, dan memperbarui halaman web secara asinkronus. Contoh penerapannya pada tugas ini adalah to do list yang akan ter-_update_ setelah penambahan task baru pada form di modal tanpa perlu melakukan _reload_ seluruh halaman.

### Implementasi
##### Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
- AJAX GET
1. Membuat fungsi baru bernama `show_json` yang menerima parameter request dan mengembalikan seluruh data task user dalam bentuk JSON.
2. Membuat path `todolist/json` pada `urls.py` yang mengarah pada fungsi `show_json`.
3. Melakukan pengambilan task menggunakan AJAX GET.
- AJAX POST
1. Membuat tombol `Add Task` yang membuka sebuah modal dengan form untuk menambahkan task.
2. Membuat fungsi baru bernama `add_todolist_item` untuk menambahkan task baru ke dalam database.
3. Membuat path `/todolist/add` yang mengarah ke `add_todolist_item`.
4. Menghubungkan form pada modal ke path `/todolist/add`.
5. Melakukan _refresh_ pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa _reload_ seluruh halaman.
