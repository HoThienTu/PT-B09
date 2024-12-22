 # Nhập hai số thực từ người dùng
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))

# Thực hiện các phép toán
tong = a + b
hieu = a - b
tich = a * b

# Kiểm tra chia cho 0
if b != 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"

# In ra kết quả
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong}")