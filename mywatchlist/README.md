[Aplikasi Heroku](https://pbp-assignment.herokuapp.com/) <br>
--> [My Watch List](https://pbp-assignment.herokuapp.com/mywatchlist/)
 <hr>
 
#### Perbedaan antara JSON, XML, dan HTML
- JSON <br>
JSON adalah singkatan dari JavaScript Object Notation. Dari namanya sendiri, pengembangan JSON dilakukan menggunakan bahasa seperti JavaScript, bukan _markup language_ seperti HTML ataupun XML. JSON digunakan untuk merepresentasikan data dalam pasangan _key-value_ yang dapat dikonversi ke atau dari JavaScript secara mudah dengan fungsi JavaScript standar. Datanya bisa langsung diakses sebagai objek JSON dan didukung sebagian besar _browser_. JSON secara umum lebih cepat dan mudah digunakan daripada XML. Walaupun berkas JSON hanya bisa dalam UTF-8 encoding, berkas JSON lebih mudah dibaca, tetapi keamanannya kurang daripada XML.

- HTML <br>
HTML adalah singkatan dari HyperText Markup Language. Sesuai namanya, HTML merupakan kombinasi dari hypertext, yaitu yang mendefinisikan link di antara _web pages_, dan markup language yang mendfinisikan struktur teks pada _web pages_ agar di-_render_ dengan baik di _web browsers_. HTML termasuk _format driven static language_. HTML adalah suatu bahasa tersendiri yang digunakan untuk membangun struktur teks. HTML berfokus pada representasi data dan tidak melakukan transfer data. Dalam pengkodeannya, HTML tidak _case sensitive_, tidak bisa menggunakan _white spaces_, menggunakan _tags_ yang sudah ditentukan untuk menampilkan data, dan _closing_-nya tidak harus digunakan. Dokumen berkas HTML relatif kecil karena _syntax_-nya singkat dan dalam format teks.

- XML <br>
XML adalah singkatan dari eXtensible Markup Language. XML adalah suatu _content driven dynamic language_ yang menyediakan framework untuk mendefinisikan markup language. XML secara umum digunakan untuk membangun struktur, menyimpan, dan mentransfer format data atau pesan. Data XML harus di-_parse_ terlebih dahulu menggunakan XML parser. Dalam pengkodeannya, XML bersifat _case sensitive_, _tags_ digunakan untuk mendeskripsikan data, bukan untuk menampilkannya, dan _closing tags_ harus digunakan. XML dapat menggunakan beberapa ragam encoding dan lebih aman daripada JSON. Tetapi di samping itu, XML lebih kompleks daripada JSON dan dokumennya cenderung lebih besar. 

#### Alasan diperlukan _data delivery_ dalam pengimplementasian sebuah platform
Pengimplementasian suatu platform terkadang perlu mengirimkan data dari satu _stack_ ke _stack_ lainnya. Untuk menghemat kapasitas, ada berkas data yang tidak disimpan di server, tetapi di-_generate_ oleh kode program. _Data delivery_ akan membantu mengurangi kompleksitas pengembangan platform, terutama dalam hal efisiensi waktu. Di sisi lain, akurasi dan _user experience_ akan semakin baik. Implementasi _data delivery_ juga akan meningkatkan keamanan serta kualitas pemrosesan dan penyimpanan data.

#### Implementasi

- HTML dengan data JSON
1. Membuat sebuah proyek Django ato `django-app` bernama `mywatchlist`.
2. Mendaftarkan `django-app` dengan menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` pada berkas `settings.py`
3. Membuat berkas `models.py` di folder `mywatchlist` berisi model `MyWatchList` dengan variabel atau atribut dan field yang sesuai.
4. Menerapkan skema model yang telah dibuat ke dalam _database_ Django lokal.
5. Membuat berkas `inital_watchlist_data.json` di folder `fixtures` di dalam folder aplikasi `mywatchlist` berisi 10 data untuk objek `MyWatchList` dan memasukkannya data ke dalam _database_ Django lokal.
6. Membuat sebuah fungsi bernama `show_watchlist` yang menerima parameter request dan mengembalikan render pada `views.py` di folder `mywatchlist` yang akan melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
7. Membuat berkas html bernama `mywatchlist.html` di dalam sebuah folder bernama `templates` di dalam folder aplikasi `mywatchlist`. Berkas tersebut berisi data yang akan ditampilkan.
8. Membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada `views.py`. Routing dilakukan dari `urls.py`, nantinya halaman HTML dapat ditampilkan melalui _browser_. Isi dari `urls.py` adalah import fungsi dari `views.py`, variabel `app_name` yang berisi nama aplikasi, dan penambahan fungsi `show_watchlist` ke variabel `urlpatterns`.
9. Melakukan pendaftaran aplikasi dengan menambahkan path ke dalam `urls.py` yang ada di folder `project_django` pada variabel `urlpatterns`. Routing sudah selesai dan akan terlihat jika projek Django dijalankan.
10. Melakukan import models yang sudah dibuat sebelumnya ke dalam berkas `views.py`. Class tersebut akan digunakan untuk melakukan pengambilan data dari database. 
11. Menambahkan variabel `context` berisi `list_film` ke dalam fungsi `show_watchlist` untuk menyimpan hasil pemanggilan fungsi _query_ ke _model database_. Variabel tersebut akan ditambahkan sebagai parameter ketiga pada pengembalian fungsi _render_.
12. Pada berkas html `mywatchlist.html`, melakukan iterasi terhadap variabel `list_film` yang telah ikut di-_render_ ke dalam HTML untuk menampilkan daftar film ke dalam tabel.

- XML
1. Mengimpor `HttpResponse` dan `Serializer` pada berkas `views.py`.
2. Membuat sebuah variabel `data` yang menyimpan hasil _query_ dari seluruh data yang ada pada `MyWatchList`.
3. Membuat fungsi `show_xml` yang menerima parameter _request_ dan mengembalikan `HttpResponse` yang berisi parameter data hasil _query_ yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`.
4. Mengimpor fungsi `show_xml` ke berkas `urls.py`.
5. Menambahkan path url ke dalam `urlpatterns` untuk mengakses `show_xml`.

- JSON
1. Membuat fungsi `show_json` yang menerima parameter _request_ dan mengembalikan `HttpResponse` yang berisi parameter data hasil _query_ yang sudah diserialisasi menjadi JSON dan parameter `content_type="application/json"`.
2. Mengimpor fungsi `show_json` ke berkas `urls.py`.
3. Menambahkan path url ke dalam `urlpatterns` untuk mengakses `show_json`.

- Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat. <br>
Setelah `add`, `commit`, dan `push` perubahan yang dilakukan ke github, membuat aplikasi baru di Heroku dan menambahkan variabel `repository secret` ke repositori github dengan format: <br>
HEROKU_API_KEY: <VALUE_API_KEY> dan <br>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU>, dalam hal ini adalah `pbp-assignment` <br>
_Deployment_ akan berhasil dilakukan setelah _workflow_ yang gagal dijalankan kembali.

#### Postman
- HTML
![HTML](https://github.com/rahmaadnda/tugas-pbp/blob/main/Tugas%203%20-%20HTML%20Postman.jpg)
- XML
![XML](https://github.com/rahmaadnda/tugas-pbp/blob/main/Tugas%203%20-%20XML%20Postman.jpg)
- JSON
![JSON](https://github.com/rahmaadnda/tugas-pbp/blob/main/Tugas%203%20-%20JSON%20Postman.jpg)
