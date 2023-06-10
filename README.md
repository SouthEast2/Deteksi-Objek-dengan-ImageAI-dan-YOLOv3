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
2. Instal prasyarat dengan menjalankan perintah berikut:
   > pip install -r requirements.txt
3. Letakkan file model YOLOv3 (yolov3.pt) di direktori model.
4. Persiapkan gambar input yang ingin Anda deteksi dan letakkan di direktori input.

# Penggunaan
1. Buka file object_detection.py.
2. Sesuaikan jalur file model YOLOv3 jika diperlukan:
   > 'model_path = "model/yolov3.pt"'
3. Jalankan program dengan perintah berikut:
   > 'python object_detection.py'
4. Program akan mendeteksi objek dalam gambar input dan menghasilkan gambar output yang ditandai dengan kotak identifikasi objek.

Terimakasih!
