from pdf2image import convert_from_path

# Đường dẫn file PDF
pdf_path = "Full_Ho_so_thi_cong_xay_dung\Full_Kien_truc.pdf"

# Chuyển đổi PDF sang danh sách ảnh (mỗi trang là một ảnh)
images = convert_from_path(pdf_path, dpi=300)  # dpi cao giúp giữ chất lượng

# Lưu ảnh dưới dạng file PNG hoặc JPG
for i, img in enumerate(images):
    img.save(f"output_page_{i+1}.png", "PNG")
