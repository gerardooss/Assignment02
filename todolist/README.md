 # Assignment 4
https://katalog-kita-semua.herokuapp.com/todolist/
 
 ## Kegunaan {% csrf_token %} pada elemen <form> dan pengaruhnya
`{% csrf_token %}` berguna sebagai proteksi dari serangan cross-site request forgery. `{% csrf_token %}` akan men-generate token keamanan secara random yang sifatnya unique untuk setiap user session. Token keamanan ini digunakan untuk menghindari serangan dari attacker karena tanpa token yang valid, attacker tidak bisa membuat valid request ke backend server.

 ## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Kita dapat memanfaatkan tag `<input>` dengan menggunakan property name dan type.

 ## Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Ketika user mengetuk button `Add new activity` maka function `add_activity` yang terdapat pada `views.py `akan dijalankan. Function ini akan memuat class NewForm yang merupakan dasar dari sebuah form. Setelah itu user akan diarahkan untuk mengisi form yang ditampilkan pada laman web.
2. Setelah user mengisi data dan mengetuk submit button, data input akan diolah dan disimpan dalam database yang dilakukan oleh potongan code `new_task.save()`
3. Setelah data tersimpan di dalam database, function `add_activity` akan mengarahkan ke function `show_todolist` untuk menginisiasi variable berisi data terkini untuk kemudian digunakan pada laman `todolist.html`.

 ## Pengimplementasian checklist di atas.
1. Menjalankan perintah `python manage.py startapp todolist` untuk membuat file proyek baru.
2. Menambahkan `todolist` pada bagian INSTALLED_APPS pada 'settings.py' dan `path('todolist/', include('todolist.urls'))` pada file urls.py yang terdapat pada `project_django`.
3. Membuat class baru pada `models.py` yang berisi jenis-jenis data yang akan digunakan, seperti user, title, date, description, da status.
4. Menambahkan function untuk registrasi, login, dan logout user. Menambahkan file `registration.html` dan `login.html`.
5. Membuat file `todolist.html` untuk mengatur tampilan website yang menunjukkan task list user. Pada file ini terdapat button untuk menambah task.
6. Membuat class `NewForms()` yang berisi kompenen data yang diperlukan. Membuat `addtask.html` untuk mengatur tampilan saat menambah task.
7. Melakukan routing pada urls.py pada folder todolist dengan menambahkan 
```
path('', show_todolist, name='show_todolist'),
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('create-task/', add_activity, name='add_activity'),
```
8. Memastikan deployment ke Heroku berhasil.




# Assignment 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline; merupakan styling yang dilakukan untuk merujuk pada satu elemen spesifik saja sehingga tidak berengaruh untuk elemen yang sama di tempat lain. Kelebihan: kita bisa mengatur elemen secara detail tanpa mempengaruhi elemen lain. Kekurangan: membutuhkan waktu cukup lama jika mengatur elemen satu per satu.
2. Internal; styling ini akan berpengaruh terhadap elemen-elemen dalam satu file. Kelebihan: kita hanya perlu cukup mengatur styling sekali saja, tidak perlu mengulang.
3. External; kita dapat mengatur tampilan seluruh html dalam satu projek hanya dengan mengubah satu file CSS saya. Kelebihan: membutuhkan waktu singkat.

Presidensi: Inline > Internal > External --> internal paling tinggi

## Jelaskan tag HTML5 yang kamu ketahui.
Berikut adalah beberapa tag pada HTML5 yang saya ketahui
`<h1> - <h6>` untuk membuat header (semakin h1 lebih tebal dibanding h2 dan seterusnya). `<form>` untuk menampilkan form pada website. `<p>` untuk penulisan teks pada website. `<table>` untuk membuat table pada website. `<style>` untuk melakukan internal styling.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Element Selector, styling berdasarkan tag, contoh `h1{...}`
2. ID Selector, merujuk pada elemen yang memiliki id, contoh `#idname{...}`
3. Class Selecter, merujuk pada elemen yang memiliki class yang sesuai, contoh `.login{...}`
4. Universal selector,styling untuk semua elemen, ditandai dengan penggunaan `*{...}`

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menghubungkan bootstrap framefork pada `base.html`
2. Membuat sebuah static file untuk melakukan external styling. Menjalankan command `python manage.py collectstatic`.
3. Menghubungkan eksternal styling dengan file html yang diinginkan dengan potongan code `<link rel="stylesheet" href="{% static 'todo/style.css' %}">`
