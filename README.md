# Link Aplikasi Heroku
[https://katalog-kita-semua.herokuapp.com/katalog/details/]


# Bagan yang berisi request client
Client --internet--> Server Django (manage.py -> views.py -> katalog.html) --internet--> Web Page

Ketika user memasukkan url pada browser berarti user melakukan request. Request ini dilakukan lewat medium internet untuk terhubung dengan server Django.

Berikutnya, server django akan menjalankan manage.py kemudian akan diteruskan ke views.py yang melibatkan models.py. models.py menggunakan data yang diambil dari database. Views.py akan mengembalikan hasil render dari katalog.html yang kemudian akan ditampilkan laman web page. Setelah itu, lewat medium internet lagi, web page akan ditampilkan pada perangkat client sebagai response dari request user.


# Penggunaan Virtual Environtment
Project python seringkali membutuhkan dependent yang berbeda-beda. Virtual Environtment berguna untuk mengisolasi package/dependent aplikasi agar tidak bertabrakan dengan versi lain.


# Implementasi pada Tugas 2
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
    > Melakukan import dari katalog.models.
    > Membuat sebuah function untuk memasukkan data yang diambil ke dalam sebuah variable untuk diteruskan ke HTML.

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py
    > Melakukan import dari katalog.views agar dapat memanggil function yang sudah dibuat pada nomor 1.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template
    > Menggunakan variable yang dibuat pada function sblmnya pada katalog.html.

4. Melakukan deployment ke Heroku terhadap aplikasi yang telah dibuat
    > Menambahkan repository secret pada gitlab berupa HEROKU_API_KEY dan HEROKU_APP_NAME sesuai dengan API_KEY pada Heroku dan nama aplikasinya.