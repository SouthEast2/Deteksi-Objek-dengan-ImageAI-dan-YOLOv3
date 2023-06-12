# Final Project Kecerdasan Buatan (D081) | Kelompok 13 | UPN Veteran Jawa Timur
Dosen Pengampu: Dr. Basuki Rahmat, S.Si, MT

Anggota Kelompok:
1) Ananda Bagus Priawan (21081010252)
2) Alfi Ramadhaniar (21081010072)

# Deteksi-Objek-dengan-ImageAI-dan-YOLOv3
Program sederhana untuk mendeteksi objek dalam gambar menggunakan metode YOLOv3 dan library ImageAI.

# Deskripsi
Program ini menggunakan model YOLOv3 untuk mendeteksi objek dalam gambar. Dengan menggunakan library ImageAI, program ini dapat mengidentifikasi berbagai objek seperti manusia, kendaraan, hewan, dan lainnya.

# Fitur
- Deteksi objek dengan metode YOLOv3.
- Identifikasi berbagai objek dalam gambar.
- Contoh penggunaan yang mudah dipahami.

# Prasyarat
- Python 3.x
- Library ImageAI
- Model YOLOv3

# Instalasi
1. Clone repository ini ke direktori lokal Anda.
2. Buat folder baru bernama "model" di dalam direktori program.
3. Unduh file model YOLOv3 (yolov3.pt) dari (https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/) ke komputer Anda.
4. Pindahkan file "yolov3.pt" yang sudah diunduh ke dalam folder "model" yang telah Anda buat sebelumnya.

# Penggunaan
1. Buka file object_detection.py.
2. Sesuaikan jalur file model YOLOv3:
   > 'model_path = "model/yolov3.pt"'
3. Jalankan program dengan perintah berikut:
   > 'python object_detection.py'
4. Program akan mendeteksi objek dalam gambar input dan menghasilkan gambar output yang ditandai dengan kotak identifikasi objek.

Terimakasih!
