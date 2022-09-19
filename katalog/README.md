[Aplikasi Heroku](https://katalog-pbp.herokuapp.com/) <br>
--> [Katalog](https://katalog-pbp.herokuapp.com/katalog/)
 <hr>
 
- Bagan

![Bagan](https://github.com/rahmaadnda/tugas-pbp/blob/main/Tugas%202%20PBP%20-%20Bagan.png)
Sesuai yang terlihat pada bagan, berkas ```urls.py```, ```views.py```, ```models.py```, dan ```html``` merupakan bagian dari Django App. User melakukan request client ke web melalui internet yang diteruskan ke Django App. Responnya akan berbentuk web page yang diteruskan ke user melalui internet juga.

- _Virtual environment_ digunakan untuk menghindari konflik yang bisa terjadi jika ada beberapa projek pada saat yang sama. Python akan terus melakukan _upgrade_ dan kita tidak selalu memerlukan versi yang terbaru. Sayangnya, Python tidak bisa membedakan versinya yang berbeda di suatu direktori. Penggunaan _virtual environment_ menjadikan pengunduhan Python _packages_ hanya dilakukan di suatu direktori atau folder projek yang diinginkan, tidak secara global. Jadi, virtual environment akan mengisolasi lingkungan projek Python agar setiap projek bisa memiliki _dependencies_-nya masing-masing sesuai kebutuhan. Namun, aplikasi web berbasis Django masih bisa dibuat tanpa menggunakan _virtual environment_. 

- Implementasi
1. Membuat sebuah fungsi pada ```views.py``` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML. <br>
Menambahkan fungsi bernama ```show_katalog``` yang menerima parameter request dan mengembalikan render.

2. Membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada ```views.py```. <br>
Routing dilakukan dari ```urls.py```, nantinya halaman HTML dapat ditampilkan melalui _browser_. Isi dari ```urls.py``` adalah import fungsi dari ```views.py```, variabel ```app_name``` yang berisi nama aplikasi, dan penambahan fungsi ```show_katalog``` ke variabel ```urlpatterns```.
Setelah itu, melakukan pendaftaran aplikasi ke dalam ```urls.py``` yang ada di folder ```project_django``` pada variabel ```urlpatterns```. Routing sudah selesai dan akan terlihat jika projek Django dijalankan.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template. <br>
Melakukan import models yang sudah dibuat sebelumnya ke dalam berkas ```views.py```. Class tersebut akan digunakan untuk melakukan pengambilan data dari database. Setelah itu, menambahkan variabel ke dalam fungsi ```show_katalog``` untuk menyimpan hasil pemanggilan fungsi query ke model database. Variabel tersebut akan ditambahkan sebagai parameter ketiga pada pengembalian fungsi _render_. Selanjutnya, mengubah ```Fill me!``` yang ada di dalam HTML tag pada berkas HTML untuk menampilkan nama di halaman HTML. Melakukan iterasi terhadap variabel ```list_barang``` yang telah ikut di-_render_ ke dalam HTML untuk menampilkan daftar barang ke dalam tabel.

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat. <br>
Setelah ```add```, ```commit```, dan ```push``` perubahan yang dilakukan ke github, membuat aplikasi baru di Heroku dan menambahkan variabel ```repository secret``` ke repositori github dengan format: <br>
HEROKU_API_KEY: <VALUE_API_KEY> dan <br>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU> <br>
_Deployment_ akan berhasil dilakukan setelah _workflow_ yang gagal dijalankan kembali.
