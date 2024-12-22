# Nhập số giây từ người dùng
s = int(input("Nhập số giây: "))

# Tính số giờ
gio = s // 3600
# Tính số phút còn lại
phut = (s % 3600) // 60
# Tính số giây còn lại
giay = s % 60

# In kết quả
print(f"Kết quả: {gio} giờ, {phut} phút, {giay} giây")