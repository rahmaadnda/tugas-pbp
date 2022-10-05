[Aplikasi Heroku](https://pbp-assignment.herokuapp.com/) <br>
--> [To-Do List](https://pbp-assignment.herokuapp.com/todolist/) <br>
akun 1 -> username: rahma             password: inipassword <br>
akun 2 -> username: userbaru          password: katasandi <br>
 <hr>

## Tugas 4
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


## Tugas 5
### Perbedaan, kelebihan, dan kekurangan dari Inline, Internal, dan External CSS.
- Inline CSS
Pendefinisian properti CSS ada di bagian body, menyatu dengan elemennya. Lebih spesifiknya, pendefinisian dilakukan dalam HTML _tag_-nya menggunakan atribut style. Kelebihannya adalah CSS dapat diterapkan dengan cepat, hal ini berpengaruh jika melakukan tes atau _preview_. Kelemahannya, penambahan CSS ke dalam setiap HTML memerlukan waktu dan terkadang membuat struktur dokumen menjadi kurang terorganisir. Inline style CSS tidak bisa menggunakan elemen atau kelas _pseudo_. Di samping itu, inline style merupakan prioritas utama penerapan CSS.
- Internal CSS
Pendefinisian properti CSS dilakukan di bagian head. Jenis ini umumnya lebih efektif ketika digunakan untuk memodifikasi satu dokumen HTML, tidak perlu ada berkas tambahan. Kekurangannya adalah ketika ingin memodikasi beberapa dokumen, penerapan CSS perlu dilakukan berulang kali. Selain itu, penambahan kode pada beberapa dokumen HTML akan meningkatkan ukuran halamannya sehingga waktu pemuatannya juga akan jadi lebih lama.
- External CSS
Pendefinisian properti CSS menggunakan berkas terpisah. Berkas tersebut menggunakan ekstensi .css dan hanya berisi style dari _tag_ atribut yang dimiliki HTML terkait. Berkas ini perlu dihubungkan dengan berkas HTML-nya menggunakan tag `link`. Untuk memodifikasi situs besar, cara ini akan lebih efektif karena modifikasi satu berkas .css akan diterapkan pada seluruh halaman web. Berkas HTML juga akan menjadi lebih bersih dengan ukuran yang lebih kecil. Kekurangannya adalah karena perlu mengunggah berkas terpisah, ada kemungkinan halaman web tidak ter-_render_ dengan benar sampai berkas eksternal CSS terbaca.

### Tag HTML5
- `<!--...-->`: menspesifikasi suatu komentar
- `<!DOCTYPE>`: menspesifikasi tipe dokumen 
- `<a>`: mendefinisikan suatu _hyperlink_ 
- `<body>`: menspesifikasi bagian body dari dokumen 
- `<button>`: membuat button yang interaktif
- `<div>`: menspesifikasi suatu bagian dari dokumen 
- `<form>`: mendefinisikan HTML form untuk input user
- `<head>`:	mendefinisikan bagian head yang berisi informasi dokumen
- `<h1>` sampai `<h6>`: mendefinisikan header (1 sampai 6)
- `<hr>`: membuat garis horizontal
- `<html>`: menspesifikasi root dari dokumen HTML
- `<input>`: mendefinisikan kontrol input
- `<label>`: mendefinisikan label untuk suatu kontrol input 
- `<li>`: mendefinisikan item dari list.
- `<p>`: mendefinisikan suatu paragraf 
- `<style>` : mendefinisikan informasi style, biasanya untuk CSS
- `<table>`: menspesifikasi suatu tabel
- `<td>`: menspesifikasi sel dari suatu tabel
- `<th>`: menspesifikasi header sel dari suatu tabel
- `<title>`: mendefinisikan judul dokumen
- `<tr>`: mendefinisikan baris dari tabel
- `<ul>`: mendefinisikan list yang tidak terurut

### Tipe CSS selector
- Universal selector: memilih semua elemen (tapi bisa dispesikasi, contohnya menggunakan `*|*`)
- Element selector: memilih semua elemen `<p>`
- ID selector: memilih semua elemen yang memiliki suatu id tertentu
- Class selector: memilih semua elemen dari class
- Attribute selector: memilih semua elemen yang memiliki suatu atribut tertentu
- `:` pseudo: memilih elemen berdasarkan status informasi yang tidak ada di document tree
- `::` pseudo: memilih entitas yang tidak termasuk dalam HTML

### Implementasi
