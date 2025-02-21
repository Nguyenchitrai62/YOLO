import cv2
import numpy as np
import pyautogui  # Thư viện lấy kích thước màn hình tự động

def detect_black_squares(image_path):
    # Đọc ảnh bản vẽ xây dựng (ảnh xám)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Làm mờ ảnh để giảm nhiễu
    blurred = cv2.medianBlur(image, 5)

    # Dùng ngưỡng nhị phân để làm nổi bật vùng đen
    _, binary = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)

    # Tìm các đường viền trong ảnh
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Chuyển ảnh sang màu để vẽ đường viền
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Danh sách lưu tọa độ các hình vuông
    square_coordinates = []

    # Lọc các hình vuông đen đặc
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Điều kiện lọc: Kích thước hợp lý và hình gần vuông
        if 10 < w and 10 < h and 0.8 < w/h < 1.2:
            # Cắt ROI từ ảnh nhị phân để kiểm tra mật độ điểm đen
            roi = binary[y:y+h, x:x+w]
            black_pixel_ratio = np.count_nonzero(roi == 255) / (w * h)  # Tính phần trăm pixel đen

            if black_pixel_ratio > 0.8: 
                cv2.rectangle(image_color, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Vẽ hình vuông màu đỏ
                square_coordinates.append((x, y, w, h))
                print(f"Phát hiện ô vuông đen đặc tại: x={x}, y={y}, w={w}, h={h}")

    return image_color, square_coordinates



# image_path = "kien_truc.png"
# output_image, coordinates = detect_black_squares(image_path)

# # *** Tự động lấy kích thước màn hình ***
# screen_width, screen_height = pyautogui.size()

# # Tạo cửa sổ với chế độ điều chỉnh kích thước
# cv2.namedWindow("Detected Black Squares", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Detected Black Squares", screen_width, screen_height)  # Đặt cửa sổ theo kích thước màn hình

# # Hiển thị ảnh kết quả
# cv2.imshow("Detected Black Squares", output_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Lưu danh sách tọa độ vào file
# with open("square_coordinates.txt", "w") as f:
#     for coord in coordinates:
#         f.write(f"{coord}\n")
