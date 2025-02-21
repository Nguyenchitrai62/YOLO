import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from detect_black_squares import detect_black_squares  # Import hàm nhận diện

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("APP")

        # self.showMaximized()

        # Label hiển thị ảnh
        self.image_label = QLabel(self)
        self.image_label.setText("Chọn ảnh để bắt đầu")
        self.image_label.setScaledContents(True)

        # Nút Import Ảnh
        self.import_button = QPushButton("Import Ảnh", self)
        self.import_button.clicked.connect(self.load_image)

        # Nút Chạy Nhận Diện
        self.detect_button = QPushButton("Chạy Nhận Diện", self)
        self.detect_button.setEnabled(False)
        self.detect_button.clicked.connect(self.detect_squares)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.import_button)
        layout.addWidget(self.detect_button)
        self.setLayout(layout)

        self.image_path = None

    def load_image(self):
        file_dialog = QFileDialog()
        self.image_path, _ = file_dialog.getOpenFileName(self, "Chọn ảnh", "", "Images (*.png *.jpg *.jpeg)")

        if self.image_path:
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=True))  
            self.detect_button.setEnabled(True)

    def detect_squares(self):
        if not self.image_path:
            return

        processed_image, _ = detect_black_squares(self.image_path)

        height, width, channel = processed_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(processed_image.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
        self.image_label.setPixmap(QPixmap.fromImage(q_img).scaled(self.image_label.size(), aspectRatioMode=True))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.showMaximized()  
    sys.exit(app.exec())
