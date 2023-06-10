import os
from imageai.Detection import ObjectDetection

# Buat objek deteksi objek
detector = ObjectDetection()

# Tentukan jalur ke model pre-trained
model_path = "model/yolov3.pt"  # Ganti dengan jalur yang sesuai dengan model dipilih

# Tentukan jalur ke file input gambar
input_folder = "input/"
input_file = "cat.jpg"  # Ganti sesuai dengan nama file gambar yang ingin diinput
input_path = os.path.join(input_folder, input_file)

# Tentukan jalur untuk folder output
output_folder = "output/"
os.makedirs(output_folder, exist_ok=True)  # Buat folder output jika belum ada

# Set model deteksi objek
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# Deteksi objek pada gambar input
output_file = "output_" + os.path.splitext(input_file)[0] + ".jpg"  # Nama output mengikuti nama file input
output_path = os.path.join(output_folder, output_file)

detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

# Tampilkan hasil deteksi objek
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"])
