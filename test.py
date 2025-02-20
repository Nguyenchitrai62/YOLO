import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# Đọc ảnh bản vẽ kiến trúc
IMAGE_PATH = "kien_truc.png"  # Thay bằng đường dẫn thực tế
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

# Danh sách các template cần kiểm tra
TEMPLATE_DIR = "templates/"  # Thư mục chứa các template
template_paths = glob.glob(TEMPLATE_DIR + "*.png")  # Lấy tất cả file ảnh trong thư mục

# Chuyển ảnh sang màu để vẽ khung hình chữ nhật
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

THRESHOLD = 0.7  # Ngưỡng để xác định vùng giống với template

for template_path in template_paths:
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    h, w = template.shape

    # Áp dụng Template Matching
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= THRESHOLD)

    # Vẽ khung chữ nhật trên ảnh gốc
    for pt in zip(*locations[::-1]):
        cv2.rectangle(image_color, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Hiển thị kết quả
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title("Phát hiện nhiều đối tượng bằng Template Matching")
plt.axis("off")
plt.show()
