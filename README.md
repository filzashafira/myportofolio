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


### Tugas 2

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
