Nama : Filza Shafira
NPM : 2506623641
Kelas : PBP C
Latihan Branching


Tugas 1

1. Penggunaan Elemen Semantik HTML5:
   Iya, aku pakai elemen semantik HTML5 kayak <header> buat bagian atas, <nav> buat navigasi, <section> buat ngebagi tiap bagian (Profile, Education, Experience, dll), sama <article> buat ngebungkus kartu skill dan project.

2. Tantangan Tata Letak CSS Responsive:
   Tantangan terbesarnya ngatur tata letak yang ada gambarnya, kayak logo di Education serta foto di Experience dan Projects. Di laptop posisinya rapi di samping teks, tapi di layar HP jadi sempit dan dorong tulisan.
   
   Cara ngatasinya, aku gunain Flexbox media queries. Posisi gambar di HP diubah dari samping jadi menumpuk di atas teks, terus ukuran gambar sama padding-nya diperkecil dikit dan tentu saja teks tetap diprioritaskan ukurannya biar nyaman dibaca tanpa bikin layout kepotong ke samping.


3. Batasan Static Web & Fungsionalitas Dinamis yang Diinginkan:
   Keterbatasan utama web statis ini yaitu semua datanya masih di-hardcode langsung di file HTML. Jadi kalau mau nambah project baru, ngubah riwayat pendidikan, atau memperbarui skill, aku harus buka dan edit kode HTML-nya manual satu per satu.

   Untuk iterasi selanjutnya, fungsionalitas dinamis yang paling ingin ditambahkan adalah integrasi database (seperti PostgreSQL/SQLite) dan arsitektur MVT Django. Fitur yang paling diprioritaskan yaitu Admin Panel buat kelola data portofolio secara otomatis, plus fitur formulir Contact Me yang bisa menyimpan pesan dari pengunjung langsung ke database.

---

AI Disclosure
Dalam pengerjaan Individual Assignment 1 ini, aku nanya-nanya dan dibantu sama AI (Gemini) buat:
Membantu penyusunan struktur HTML semantik, memberikan saran CSS Flexbox agar tampilan responsif di HP, merapikan rata kanan kiri deskripsi section.

Semua saran dari AI tetap aku tes, sesuaikan, dan jalankan sendiri secara lokal(python manage.py runserver) maupun di PWS untuk memastikan kodeknua berjalan lancar tanpa adanya error.


Tugas 2

#### 1. Alur Pemrosesan Permintaan (Request-Response Cycle) MVT pada Django

Ketika pengguna membuka halaman portofolio baru (misalnya halaman **Education** di `/education/`), terjadi alur komunikasi terstruktur berbasis pola arsitektur **Model-View-Template (MVT)** sebagai berikut:

1. **HTTP Request dari Browser:**
   - Pengguna mengetikkan URL atau mengklik tautan navigasi (`<a href="...">`) di browser. Browser mengirimkan berkas *HTTP Request* ke server Django.

2. **Routing Tingkat Proyek (`myportfolio/urls.py`):**
   - Perintah masuk pertama kali ditangkap oleh file konfigurasi rute utama proyek (`urls.py` milik proyek).
   - Proyek memeriksa *path* URL yang diminta. Menggunakan fungsi `include('main.urls')`, Django memforward/meneruskan penanganan pemetaan URL tersebut ke file routing tingkat aplikasi (`main/urls.py`).

3. **Routing Tingkat Aplikasi (`main/urls.py`):**
   - File `main/urls.py` mencocokkan pola string URL `/education/` dengan daftar `urlpatterns`.
   - Setelah menemukan pasangan rute `path('education/', show_education, name='show_education')`, Django memanggil fungsi penanganan (*controller/view*) bernama `show_education` yang berada di `main/views.py`.

4. **Eksekusi Logika Bisnis & Pengambilan Data (`main/views.py` & `main/models.py`):**
   - Fungsi `show_education` dieksekusi.
   - View berkomunikasi dengan **Model** `Education` dengan memanggil *query* ORM Django: `Education.objects.all()`.
   - **Model (`main/models.py`)** melakukan kueri ke database (`db.sqlite3`), mengambil seluruh baris data riwayat pendidikan, lalu mengembalikannya ke View dalam bentuk *QuerySet* (kumpulan objek Python).
   - View membungkus data tersebut ke dalam sebuah *Python Dictionary* yang dinamakan `context` (misal: `{'education_list': education_list}`).

5. **Rendering Template & Pemrosesan HTML (`main/templates/education.html`):**
   - View memanggil fungsi `render(request, 'education.html', context)`.
   - **Django Template Engine** menggabungkan struktur HTML statis pada `education.html` dengan data dinamis dari `context`.
   - *Django Template Language (DTL)* memproses sintaksis khusus:
     - Logika perulangan `{% for edu in education_list %}` mengekstraksi atribut tiap objek (seperti `{{ edu.institution }}`, `{{ edu.degree }}`, `{{ edu.start_year }}`).
     - Kondisi `{% empty %}` menangani persyarat alternatif jika *QuerySet* kosong.
     - Tag `{% static 'css/style.css' %}` memuat aset CSS eksternal.
   - Engine menerjemahkan seluruh tag DTL menjadi kode HTML murni yang siap dibaca oleh browser.

6. **HTTP Response ke Browser:**
   - View mengembalikan berkas HTML utuh yang sudah di-render sebagai *HTTP Response* (dengan status code `200 OK`) kembali ke browser pengguna untuk ditampilkan secara visual.

---

#### 2. Alasan Penggunaan Model vs. Hard-coding pada Template serta Dampaknya

Menyimpan data portofolio pada **Model** (database) ketimbang menulisnya secara langsung (*hard-code*) di dalam berkas HTML template memberikan dampak krusial terhadap pemeliharaan dan pengembangan perangkat lunak:

1. **Pemisahan Tanggung Jawab (*Separation of Concerns*):**
   - **Template** hanya bertanggung jawab atas **presentasi visual** (struktur UI, tata letak CSS, dan animasi JS).
   - **Model** bertanggung jawab atas **struktur dan integritas data**.
   - Ketika ada perubahan data (misal: pembaruan deskripsi atau tahun kelulusan), pengembang tidak perlu menyentuh atau berisiko merusak struktur markup HTML/CSS.

2. **Kemudahan Pemeliharaan (*Maintainability*):**
   - Pembaruan data dapat dilakukan secara mandiri melalui antarmuka **Django Admin** tanpa perlu mengubah kode sumber (*source code*) aplikasi dan tanpa perlu melakukan proses *re-deploy* atau *commit* ulang ke Git.

3. **Skalabilitas dan Efisiensi Kode (*Scalability & DRY Principle*):**
   - Menerapkan prinsip *Don't Repeat Yourself (DRY)*. Cukup dengan membuat satu blok komponen struktur HTML di dalam perulangan `{% for %}`, halaman mampu menampilkan puluhan hingga ratusan data pendidikan secara otomatis dan konsisten.

4. **Fleksibilitas Pengolahan Data:**
   - Data yang tersimpan di Model dapat dengan mudah diurutkan (*sorting*), difilter, atau dihubungkan (*relationship*) dengan tabel lain di masa mendatang.

---

#### 3. Perbedaan `makemigrations` dan `migrate` pada Django

Kedua perintah ini merupakan bagian dari sistem manajemen skema database (ORM Migration System) di Django:

| Fitur / Perintah | `python manage.py makemigrations` | `python manage.py migrate` |
| :--- | :--- | :--- |
| **Fungsi Utama** | Membaca perubahan pada `models.py` dan **membuat berkas instruksi/skenario migrasi baru** di folder `migrations/`. | **Menerapkan/mengesekusi** berkas instruksi migrasi tersebut ke dalam database nyata (`db.sqlite3`). |
| **Dampak ke Database** | **Tidak mengubah** isi atau struktur tabel database secara langsung. Hanya menghasilkan file Python baru (contoh: `0001_initial.py`). | **Mengubah struktur fisik database** (membuat tabel baru, mengubah kolom, atau menghapus tabel). |
| **Analogi** | Membuat Cetak Biru / Denah Bangunan (*Blueprint*). | Membangun fisik bangunan berdasarkan cetak biru tersebut. |

**Contoh Kasus Perubahan Model:**
Misalkan kita ingin menambahkan field baru `thumbnail` untuk menyimpan URL logo instansi pada model `Education` di `main/models.py`:

```python
class Education(models.Model):
    institution = models.CharField(max_weight=255)
    degree = models.CharField(max_length=255)
    start_year = models.IntegerField()
    # Menambahkan field baru:
    thumbnail = models.URLField(blank=True, null=True)


AI Disclosure
Dalam pengerjaan Individual Assignment 1 ini, aku nanya-nanya dan dibantu sama AI (Gemini) buat:
Membantu penyusunan struktur HTML semantik, memberikan saran CSS Flexbox agar tampilan responsif di HP, merapikan rata kanan kiri deskripsi section.

Semua saran dari AI tetap aku tes, sesuaikan, dan jalankan sendiri secara lokal(python manage.py runserver) maupun di PWS untuk memastikan kodeknua berjalan lancar tanpa adanya error.


### Tugas 3

1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

Penggunaan ModelForm vs Form HTML Manual:
Pertama, mengenai otomatisasi dan efisiensi kode atau prinsip Don't Repeat Yourself. Saat menggunakan form HTML manual, kita harus menulis tag input satu per satu, mengelola atribut nama, tipe data, serta pesan validasi secara manual di HTML, lalu mengekstrak nilai request.POST.get() satu per satu di view. ModelForm secara otomatis membuat komponen form beserta tipe widget HTML yang sesuai berdasarkan skema atau field yang ada pada Model Django.

Kedua, mengenai validasi data yang terintegrasi. ModelForm secara otomatis menerapkan aturan validasi dari model seperti max_length, null=False, tipe data email, integer, dan lainnya. Method form.is_valid() mengeksekusi pemeriksaan keamanan dan sanitasi data input secara menyeluruh sebelum disimpan ke basis data melalui form.save().

Ketiga, mengenai keamanan dan sanitasi input. ModelForm menangani sanitasi input untuk mencegah celah keamanan seperti SQL Injection dan Cross-Site Scripting (XSS) secara otomatis saat data disimpan ke basis data.

Kewajiban Menambahkan {% csrf_token %}:

Pencegahan serangan CSRF (Cross-Site Request Forgery). Serangan CSRF terjadi ketika situs berbahaya memaksa browser pengguna yang sedang terautentikasi untuk mengirimkan permintaan POST yang tidak diinginkan ke server aplikasi kita tanpa sepengetahuan pengguna.

Mekanisme kerja token. Tag {% csrf_token %} menyisipkan sebuah input rahasia bertipe hidden yang berisi token unik terenkripsi pada form HTML. Saat form di-submit, middleware Django (CsrfViewMiddleware) akan membandingkan token dari form dengan token yang ada pada session atau cookie pengguna. Jika token tidak cocok atau hilang, Django akan menolak permintaan tersebut dengan respons 403 Forbidden.

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

Ukuran data lebih ringan dan efisien. JSON (JavaScript Object Notation) menggunakan sintaks berbasis pasangan key-value dan kurung siku atau kurawal yang ringkas. Sebaliknya, XML (eXtensible Markup Language) memerlukan tag pembuka dan penutup yang panjang, sehingga ukuran payload XML jauh lebih besar dan menghabiskan lebih banyak bandwidth jaringan.

Kecepatan parsing dan integrasi native dengan JavaScript. Dalam ekosistem front-end modern seperti React, Vue, atau Vanilla JS, JSON secara native langsung dipetakan menjadi objek JavaScript melalui fungsi bawaan JSON.parse(). Sementara XML memerlukan proses parsing DOM Parser yang jauh lebih lambat, kompleks, dan memakan memori CPU browser untuk mengakses elemen-elemennya.

Kemudahan dibaca manusia dan mesin. Struktur data JSON seperti array dan object sangat intuitif serta cocok dengan struktur data dasar pada sebagian besar bahasa pemrograman modern, contohnya Dictionary dan List pada Python atau Map dan Object pada JavaScript.

Standar RESTful API modern. Mayoritas API modern dan layanan cloud menggunakan JSON sebagai format standar transmisi data karena efisiensi deserialisasi pada komunikasi client-side berbasis AJAX atau Fetch API.

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

Alur Eksekusi dari Browser ke View hingga menjadi JSON:

Langkah pertama, HTTP Request. Client atau browser mengirimkan permintaan HTTP GET ke endpoint URL JSON, misalnya /json/ atau /awards/json/.

Langkah kedua, QuerySet Retrieval. Fungsi view di Django menerima permintaan dan mengambil data dari basis data menggunakan QuerySet ORM, contohnya data = Award.objects.all().

Langkah ketiga, Serialization Process. Data QuerySet tersebut diubah formatnya menjadi bentuk yang universal seperti daftar dictionary Python menggunakan modul django.core.serializers.

Langkah keempat, HTTP Response. Data hasil serialisasi kemudian dibungkus dalam objek HttpResponse(data, content_type="application/json") atau JsonResponse untuk dikirimkan kembali ke client dengan header HTTP JSON yang sesuai.

Alasan Perlunya Proses Serialization:

Objek QuerySet Django yang dikembalikan oleh ORM seperti Award.objects.all() adalah objek Python kompleks yang berisi logika internal Django seperti metode relasi database, caching, dan lainnya. Sementara itu, teks JSON hanya dapat merepresentasikan tipe data primitif atau sederhana seperti string, number, boolean, array, dan null.

Serialization adalah proses penerjemahan atau konversi dari objek kompleks Python atau Django ORM tersebut menjadi format teks terstruktur (JSON) agar dapat dikirimkan melalui jaringan internet dan dibaca oleh bahasa pemrograman apa pun di sisi client seperti JavaScript di browser.

### AI Disclosure

Dalam pengerjaan Individual Assignment 3 ini, saya menggunakan bantuan AI (Gemini) sebagai alat bantu diskusi, penyusunan struktur, dan debugging:

1. Peran AI dalam Pengerjaan:
* Membantu penyusunan struktur HTML semantik untuk template halaman.
* Memberikan saran tata letak CSS Flexbox dan CSS Grid agar tampilan antarmuka responsif saat diakses dari perangkat seluler.
* Menganalisis log kesalahan terminal seperti FieldError pada forms.py dan OperationalError saat pembuatan model baru, serta memberikan arahan perbaikan kode.
* Membantu menyusun kerangka penjelasan reflektif secara terstruktur dan komprehensif.


2. Verifikasi dan Pengujian Mandiri:
* Seluruh saran kode, potongan skrip, dan instruksi dari AI selalu saya pelajari, uji coba, sesuaikan, dan jalankan secara mandiri di lingkungan lokal (python manage.py runserver) serta di lingkungan deployment Pacil Web Service untuk memastikan seluruh fungsionalitas berjalan lancar tanpa adanya error.