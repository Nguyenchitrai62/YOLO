import json
import os

input_dir = "labelme_json/"  # Thư mục chứa file .json của Labelme
output_dir = "yolo_labels/"  # Thư mục để lưu file .txt YOLO

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith(".json"):
        json_path = os.path.join(input_dir, file)
        with open(json_path, 'r') as f:
            data = json.load(f)

        image_width = data["imageWidth"]
        image_height = data["imageHeight"]
        txt_filename = os.path.join(output_dir, file.replace(".json", ".txt"))

        with open(txt_filename, "w") as txt_file:
            for shape in data["shapes"]:
                label = 0  # "Tường" là class 0
                points = shape["points"]

                x_min = min(p[0] for p in points)
                x_max = max(p[0] for p in points)
                y_min = min(p[1] for p in points)
                y_max = max(p[1] for p in points)

                x_center = (x_min + x_max) / 2 / image_width
                y_center = (y_min + y_max) / 2 / image_height
                width = (x_max - x_min) / image_width
                height = (y_max - y_min) / image_height

                txt_file.write(f"{label} {x_center} {y_center} {width} {height}\n")
