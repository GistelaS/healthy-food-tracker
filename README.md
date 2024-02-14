# Healthy Food Tracker
## Tugas 2
- ### Membuat sebuah proyek Django baru

    a. Langkah pertama adalah saya membuat          direktori baru yang bernama healthy-food-tracker pada komputer saya lalu saya membuka command prompt dan membuat virtual environment dengan perintah 

   ```
    python -m venv env 
   ```
   Lalu setelah menambahkan virtual enviroment,tidak lupa untuk menjalankan virtual environment dengan perintah sebagai berikut 

   ```
   env\Scripts\activate
   ```
   Dengan begitu sudah keluar tanda aktifnya virtual environment dengan (env) dibagaian paling depan setiap perintah di command prompter.

    b. Selanjutnya saya mengisolasi         dependencies dan menciptakan proyek Django yang baru.Yang pertama dalam tahap ini saya menambahkan di dalam folder Healthy-Food-Tracker yaitu berkas requirements.txt yang akan diisi dengan dependencies yaitu

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    Setelah itu saya melakukan instalasi dependencies dan tetap menajalankan virtual environment yang sudsah saya jalankan sebelumnya. Perintah yang saya jalankan di command prompter adalah 
    ```
    pip install -r requirements.txt
    ```
    Lalu menambahkan proyek baru yang bernama healthy_food_tracker dengan perintah di command prompter 
    ```
    django-admin startproject healthy_food_tracker .
    ```
    c. Saya juga melakukan konfigurasi  setelahnya dan     tidak lupa menjalankan server dengan menambahkan tanda bintang diantar kurung dibagian ALLOWED_HOSTS yang ada di settings.py (kalau saya menggunakan visual studio code) yang berguna untuk deployment dengan perintah
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
    Step berikutnya saya membuka berkas manage.py pada direktori yang sudah diaktifkan pada command prompter sebelumnya yang sudah dijalankan. Menggunakan server Django dan memberi perintah 
    ```
    python manage.py runserver
    ```
    Karena saya menggunakan windows maka saya menggunakan perintah itu. Dan untuk memastikan keberhasilan Django yang telah saya buat, saya membuka link ini http://localhost:8000/ dan saya mendapatkan animasi roket yang aktif dan artinya sudah berhasil.

 - ### Membuat aplikasi dengan nama main pada proyek tersebut.
    
    a. Pada bagian ini, untuk membuat aplikasi baru saya melakukannya dengan perintah di command prompter yang sudah dijalankan virtual environment sebelumnya yaitu
    ```
    python manage.py startapp main
    ```
    Dengan perintah yang diatas, terciptalah direktori baru dengan nama main yang berisis struktur awal mengenai aplikasi yang akan saya buat .

    Lalu saya buka visual studio code dan mendaftarkan aplikasi main ke dalam proyek. Saya membuka berkasi settings.py yang ada didalam direktori proyek healthy
    _food_tracker dan mencari variabel INSTALLED_APPS dan menambahkan 'main' seperti ini
    ```
    INSTALLED_APPS = [
    ...,
    'main',
    ...
    ]
    ```


 - ### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    
    A. name sebagai nama item dengan tipe CharField.

    B. amount sebagai jumlah item dengan tipe IntegerField.

    C. description sebagai deskripsi item dengan tipe TextField.

    a. Untuk tahap ini pertama saya membuka berkas models.py yang ada di dalam aplikasi main pada visual studio code saya dan mengisi berkas tersebut dengan kode ini
    ```
    from django.db import models

    class food(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    calories = models.IntegerField()
    description = models.TextField()
    ```


 - ### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    a. Dan tahap ini saya hanya mengecek apakah sudahnya ada perintah didalam berkas views.py yang terletak di berkas aplikasi main saya pada visual studio code saya.Berikut perintah yang saya cek 

    ```
    from django.shortcuts import render
    ```

    Dan memang sudah ada. Setelah itu saya menambahkan lagi isi dibawah from django.shortcuts import render, dengan

    ```
    def show_main(request):
    context = {
        'name': 'Gistela Namasya Sinurat',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
    ```


 - ### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- ### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

    Dan untuk kedua poin ini akan saya paparkan dengan bersamaan. 
    a. Pertama saya menambahkan new file pada visual studio code saya dengan nama urls.py dan menambahkannya kedalam berkas main. Lalu saya membuka berkas urls.py di visual studio code saya yang sebelumnya ada di berkas healthy_food_tracker dan mencari from django.urls import path dan menambahkan , include disampingnya. Dan juga saya merubah variabel urlpatterns . menjadi

    ```
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
    ```

- ### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

- ### Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

A. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    A. Untuk poin ini sudah saya paparkan di berkas README. md ini

    B. Susah ada penjelasan di atas.

    C. Virtual environment (lingkungan virtual) adalah alat yang memungkinkan Anda untuk membuat lingkungan Python terisolasi. ada beberapa alasan digunakannya virtual enviroment dalam pengembangan aplikasi web berbasis Django : Isolasi Dependensi:  Dengan virtual environment, Anda dapat memiliki beberapa versi Python di komputer Anda tanpa bentrokan. Setiap versi dapat dianggap sebagai lingkungan pengembangan yang terpisah. Anda dapat menginstal versi berbeda dari pustaka dan modul Python secara terisolasi. Ini sangat penting karena memungkinkan Anda menghindari konflik antara versi ketika bekerja pada beberapa proyek. 

    1.	Isolasi Dependensi      Virtual environment dapat memeberi pengguna untuk memiliki beberapa versi python dikomputernya tanpa bentrok. Di tiap versi bisa dianggap sebagai lingkungan pengembangan yang terpisah. Dan juga pengguna dapat menginstal versi berbeda dari pustaka dan modul python secara terisolasi. Penting adanya karena dapat memberikan kemungkinan untuk terhindar dari konfil antara versi di berbagai pekerjaan proyek pengguna.

    2.	Kepatuahn Versi 
    Virtual environment memberikan kemungkinan para pengguna dalam menentukan dan mengelola versi yang tepat dari Django dan dependensinya untuk di berbagai proyek. Dapat memastikan untuk proyek pengguna pasti kompatibel dengan versi yang digunakan saat pengembangan, walaupun nantinya pengguna ingin mengupgrade Django ataupun pustaka lain untuk berbagai proyek.

    3.	Kebersihan dan Keamanan
    Adanya Virtual environment, pengguna dapat memastikan pengembangan dan pemeliharaan proyek Django dan tidak mengkhawatirkan konflik dependensi.

    4.	Pengujian
    Pengujian sangat penting untuk virtual environment. Jika pengguna hendak mengganti versi Django didalam aplikasi web dari 1.5 ke 1.9, pengguna tiak sulit untuk menjalankannya dan membuat virtuak environment yang baru lalu dapat menginstal versi Django yang lain.

    Walaupun pengguna tidak diwajibkan untuk menggunakan virtual environment, lebih baik dan disarankan agar pengguna tetap menggunakannya dengan cara pengaplikasian yang mudah yaitu membuat virtual environment yang baru lalu mengaktifkan virtual environment dan akhirnya bisa mengembangkan aplikasi web dajngo yang jauh dari konflik dependensi.

    D. 

    1. Model-View-Controller (MVC):
    - Model: Mewakili data dan bisnis logic aplikasi.
    - View: Bertanggung jawab untuk menampilkan data dari model.
     - Controller: Berperan sebagai penghubung antara model     dan view. Mengatur interaksi pengguna dan mengubah status model dan view.
     - *Perbedaan: Pada MVC, view adalah struktur aktif yang meminta informasi dari model. Controller hanya mengubah status model dan view.

    2. Model-View-Template (MVT):
     - Model: Sama seperti pada MVC, mewakili data dan bisnis logic.
     - View: Menampilkan data dari model.
    - Template: Bertanggung jawab untuk menghasilkan tampilan HTML. Mirip dengan view pada MVC.
     - *Perbedaan*: MVT adalah varian dari MVC yang lebih umum digunakan dalam kerangka kerja web Django. Template menggantikan peran view dalam menghasilkan tampilan.

    3. Model-View-ViewModel (MVVM):
     - Model: Data dan bisnis logic, sama seperti pada MVC dan MVT.
     - View: Menampilkan data dari model.
     - ViewModel: Berperan sebagai penghubung antara view dan model. ViewModel memanipulasi informasi sebelum melewatkan ke view.
     - Perbedaan: MVVM digunakan ketika ada antarmuka pengguna yang sudah ada (misalnya, UI yang tidak dapat diubah) dan model yang sudah ada. ViewModel membantu mengintegrasikan keduanya.

    secara singkat:
    - MVC: View aktif, controller mengubah model dan view.
    - MVT: Mirip dengan MVC, tetapi menggunakan template untuk tampilan.
    - MVVM: ViewModel memanipulasi data sebelum ditampilkan di view.

## Tugas 3

- ### Membuat input form untuk menambahkan objek model pada app sebelumnya.

   Pertama saya menambahkan file baru pada direktori utama saya yang bernama base.html yang diisi dengan kode berikut :
   ```
      {% load static %}
   <!DOCTYPE html>
   <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
      </head>

      <body>
      {% block content %} {% endblock content %}
      </body>
   </html> 
   ```


   Setelah itu saya membuka settings.py yang ada pada direktori templates di direktori healthy_food_tracker dan mengubah sebagian menjadi kode berikut :
   ```
   TEMPLATES = [
      {
         'BACKEND': 'django.template.backends.django DjangoTemplates',
         'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
         'APP_DIRS': True,
         ...
      }
   ]
   ```

   Langkah selanjutnya saya menambah file baru dan memasukkannya ke direktori main melalu visual studio code dan mengisi dengan kode berikut :
   ```
   from django.forms import ModelForm
   from main.models import Food

   class FoodFormBookForm(ModelForm):
      class Meta:
        model = Food
        fields = ["name", "calories", "description"]   
   ```

   Dan setelah itu saya membuka direktori views.py pada direktori main dan menambahkan beberaoa kode kedalamnya di bagian paling atas yaitu :
   ```
   from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
   from main.forms import FoodForm
   from main.models import Food
   ```

   Masih di file yang sama yaitu file viewa.py saya menambahkan kode yang berguna untuk menambah jenis makanan sehat di formulir secara otomatis ketika meng submit di formulir yang akan diciptakan dengan :
   ```
   def create_food(request):
    form = FoodForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food.html", context)
    ```

    Saya menambahkan beberapa fungsi pada bagian show_main pada file views.py yang masih di direktori main dengan kode :
   ```
   def show_main(request):
    foods = food.objects.all()

    context = {
        'name': 'Gistela Namasya Sinurat',
        'class': 'PBP A',
        'foods': foods
    }

    return render(request, "main.html", context)
    ```

   Lalu saya membuka file urls.py yang ada di direktori main dan mengubah fungsi menjadi :
   ```
   from main.views import show_main, create_food
   ```

   Dan saya menambahkan path url tetap masih di direktori urls.py yang sama di fungsi urlpatterns dengan :
   ```
   path('create-food', create_food, name='create_food'),
   ```

   Setelah itu saya membuat file baru yang bernama create_food.html yang say masukkan ke direktori templates yang ada di direktori main dan mengisinya dengan kode :
   ```
   {% extends 'base.html' %} {% block content %}
<h1>Add New Food</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Food" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

Selanjutnya saya membuka file main.html dan menambahkan kode :
```
<table>
  <tr>
    <th>Name</th>
    <th>Page</th>
    <th>Description</th>
    <th>Date Added</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini
  {%endcomment %} {% for book in books %}
  <tr>
    <td>{{food.name}}</td>
    <td>{{food.calories}}</td>
    <td>{{food.description}}</td>
    <td>{{food.date_added}}</td>
  </tr>
  {% endfor %}
</table>

<br />

<a href="{% url 'main:create_food' %}">
  <button>Add New Food</button>
</a>
{% endblock content %}
```








