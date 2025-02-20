from ultralytics import YOLO

# Load model YOLOv8 pre-trained (bản nhỏ YOLOv8n)
model = YOLO("yolov8n.pt")

# Huấn luyện model
results = model.train(
    data="dataset/data.yaml",   # Đường dẫn đến file data.yaml
    epochs=50,                  # Số epoch huấn luyện
    imgsz=640,                  # Kích thước ảnh đầu vào (resize về 640x640)
    batch=16,                   # Kích thước batch (có thể điều chỉnh tùy thuộc vào GPU)
    device="cuda"               # Nếu có GPU, nếu không có thay "cpu"
)

