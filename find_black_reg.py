import cv2
import numpy as np

# Đọc ảnh bản vẽ xây dựng
image = cv2.imread("kien_truc.png", cv2.IMREAD_GRAYSCALE)

# Áp dụng làm mờ để giảm nhiễu
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Dùng ngưỡng nhị phân để làm nổi bật vùng đen
_, binary = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY_INV)  # THRESH_BINARY_INV để lấy vùng đen

# Tìm các đường viền trong ảnh
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Chuyển ảnh sang màu để vẽ đường viền
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Danh sách lưu tọa độ các hình vuông
square_coordinates = []

# Lọc các hình vuông đen đậm dựa vào tỷ lệ giữa chiều dài & rộng
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    
    # Điều kiện lọc: Ô vuông có kích thước phù hợp
    if 10 < w < 100 and 10 < h < 100 and 0.8 < w/h < 1.2:  # Kiểm tra hình vuông
        cv2.rectangle(image_color, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Vẽ ô vuông màu đỏ
        
        # Lưu tọa độ vào danh sách
        square_coordinates.append((x, y, w, h))
        print(f"Phát hiện ô vuông tại: x={x}, y={y}, w={w}, h={h}")

# Hiển thị ảnh kết quả
cv2.imshow("Detected Squares", image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Nếu cần lưu danh sách tọa độ vào file
with open("square_coordinates.txt", "w") as f:
    for coord in square_coordinates:
        f.write(f"{coord}\n")
