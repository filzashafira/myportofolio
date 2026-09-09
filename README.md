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
