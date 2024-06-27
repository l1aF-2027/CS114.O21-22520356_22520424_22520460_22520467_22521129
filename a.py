import os

def rename_images_in_folder(folder_path):
    # Lấy danh sách các tệp trong thư mục
    files = os.listdir(folder_path)
    # Lọc ra các tệp ảnh (có thể bạn cần điều chỉnh loại tệp ảnh tùy thuộc vào định dạng ảnh của bạn)
    image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    
    # Lặp qua từng tệp ảnh và đổi tên
    for i, image_name in enumerate(image_files):
        new_name = f"22520356-22520424-22520460-22520467-22521129.VinFast.{i+160}.jpg"
        os.rename(os.path.join(folder_path, image_name), os.path.join(folder_path, new_name))

# Thay đổi đường dẫn tới thư mục của bạn
folder_path = r"D:\Asus\Máy học - CS104\Data\VinFast"
rename_images_in_folder(folder_path)