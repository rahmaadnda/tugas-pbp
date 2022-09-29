[Aplikasi Heroku](https://pbp-assignment.herokuapp.com/) <br>
--> [To-Do List](https://pbp-assignment.herokuapp.com/todolist/) <br>
akun 1 -> username: rahma             password: inipassword <br>
akun 2 -> username: userbaru          password: katasandi <br>
 <hr>

### Kegunaan `{% csrf_token %}` pada elemen `<form>`.
Serangan Cross-Site Request Forgery (CSRF) memaksa pengguna untuk mengeksekusi sesuatu yang tidak diinginkan di dalam sebuah aplikasi web. Penyerang memanfaatkan pengguna yang telah terautentikasi dengan mengganti request dari pengguna sehingga aksi yang dilakukan tidak sesuai dengan keinginan mereka. Penyerangan yang terjadi pada akun admin dapat membahayakan web aplikasi secara keseluruhan.
 
CSRF adalah serangan yang umum sehingga Django memiliki solusi yang singkat untuk menghindarinya, yaitu dengan menggunakan tag `{% csrf_token %}` pada elemen `<form>` terkait. _Tag_ tersebut melakukan _generate_ token yang rahasia, unik, dan tidak bisa diprediksi dari server ketika melakukan _render_. Token ini akan dicek setiap ada request yang masuk. Request tidak akan dijalankan jika tidak memiliki token atau jika _value_-nya berbeda. Dengan ini, keamanan post request dari pengguna ke server akan lebih terjamin. Tidak adanya _tag_ tersebut akan meningkatkan risiko serangan CSRF.
 
### Gambaran besar cara membuat elemen `<form>` secara manual
`{{ form.as_table }}` adalah salah satu built-in methods dari Django, yaitu sebuah generator yang akan melakukan _render_ pada form sebagai tabel. Elemen `<form>` juga bisa di-_render_ tanpa menggunakan generator. Salah satu caranya adalah dengan menggunakan CSS pada berkas HTML. Pengaksesan masing-masing _field_ juga bisa dengan menggunakan atribut `{{ field }}` dan memanfaatkan atribut `{{ form }}`.

### Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada template HTML.
Setelah pengguna mengisi form dan melakukan "submit", _browser_ akan melakukan _generate_ terhadap HTTP Request, Method, dan argumennya ke URL tujuan berdasarkan halaman form HTML. Server menerima HTTP request dan menentukan fungsi dari `views.py` yang terpanggil. Fungsi tersebut akan dijalankan, penyimpanan data ke _database_ dilakukan di dalamnya dan fungsi tersebut akan mengembalikan hasil _generate_ halaman HTML untuk ditampilkan di _browser_ dan diteruskan ke pengguna.

### Implementasi
1. Membuat sebuah proyek Django atau `django-app` bernama `todolist`.
2. Mendaftarkan `django-app` dengan menambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APPS` pada berkas `settings.py`
3. Membuat berkas `models.py` di folder `todolist` berisi model `Task` dengan variabel atau atribut dan yang sesuai.
4. Membuat berkas `forms.py` di folder `todolist` untuk menyimpan atribut dari form.
5. Menerapkan skema model yang telah dibuat ke dalam _database_ Django lokal (melakukan migrate).
6. Melakukan import models yang sudah dibuat sebelumnya ke dalam berkas `views.py`. Class tersebut akan digunakan untuk melakukan pengambilan data dari database. 
7. Membuat sebuah fungsi bernama `show_todolist` yang menerima parameter request dan mengembalikan render pada `views.py` di folder `todolist` yang akan melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah berkas HTML.
8. Membuat berkas HTML bernama `todolist.html` di dalam sebuah folder bernama `templates` di dalam folder aplikasi `todolist`. Berkas tersebut berisi data yang akan ditampilkan.
9. Menambahkan variabel `context` berisi `list_task` ke dalam fungsi `show_todolist` untuk menyimpan hasil pemanggilan fungsi _query_ ke _model database_. Melakukan iterasi terhadap variabel `list_task` untuk menampilkan daftar _task_ ke dalam tabel. Variabel `context` akan ditambahkan sebagai parameter ketiga pada pengembalian fungsi _render_.
10. Membuat sebuah fungsi bernama `register` yang menerima parameter request dan mengembalikan render pada `views.py` di folder `todolist` yang akan melakukan pendaftaran akun pengguna dan dikembalikan ke dalam sebuah berkas HTML.
11. Membuat berkas HTML bernama `register.html` di dalam sebuah folder bernama `templates` di dalam folder aplikasi `todolist`. Berkas tersebut merupakan tampilan formulir registrasi.
12. Membuat sebuah fungsi bernama `login_user` yang menerima parameter request dan mengembalikan render pada `views.py` di folder `todolist` yang akan melakukan login pengguna sesuai input dan dikembalikan ke dalam sebuah berkas HTML.
13. Membuat berkas HTML bernama `login.html` di dalam sebuah folder bernama `templates` di dalam folder aplikasi `todolist`. Berkas tersebut merupakan halaman awal yang akan mengarahkan pengguna untuk login.
14. Membuat sebuah fungsi bernama `logout_user` yang menerima parameter request dan mengembalikan render pada `views.py` di folder `todolist` yang akan melakukan logout pengguna.
15. Membuat sebuah fungsi bernama `create_task` yang menerima parameter request dan mengembalikan render pada `views.py` di folder `todolist` yang akan melakukan pengambilan dan penyimpanan data dari input user, dikembalikan ke dalam sebuah berkas HTML.
16. Membuat berkas HTML bernama `create-task.html` di dalam sebuah folder bernama `templates` di dalam folder aplikasi `todolist`. Berkas tersebut merupakan tampilan formulir penambahan tugas.
17. Membuat routing untuk memetakan fungsi yang telah dibuat pada `views.py`. Routing dilakukan dari `urls.py`, nantinya halaman HTML dapat ditampilkan melalui _browser_. Isi dari `urls.py` adalah import fungsi dari `views.py`, variabel `app_name` yang berisi nama aplikasi, dan penambahan fungsi ke variabel `urlpatterns`.
18. Melakukan pendaftaran aplikasi dengan menambahkan path ke dalam `urls.py` yang ada di folder `project_django` pada variabel `urlpatterns`. Routing sudah selesai dan akan terlihat jika projek Django dijalankan.
19. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat. <br>
Setelah `add`, `commit`, dan `push` perubahan yang dilakukan ke github, menjalankan _deployment_ ulang.
20. Menjalankan aplikasi di situs web Heroku dan membuat dua akun pengguna, tiga _dummy_ data pada akun masing-masing.
