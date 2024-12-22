# Nhập độ tuổi của người dùng
tuoi = int(input("Nhập tuổi: "))

# Kiểm tra và tính giá vé dựa trên độ tuổi
if tuoi < 12:
    gia_ve = 50000  # Trẻ em dưới 12 tuổi
elif 12 <= tuoi <= 60:
    gia_ve = 100000  # Người lớn từ 12 đến 60 tuổi
else:
    gia_ve = 70000  # Người cao tuổi trên 60 tuổi

# In ra giá vé
print(f"Giá vé: {gia_ve} VNĐ")