# Nhập chiều cao của An, Minh, và Lan
chieu_cao_An = float(input("Nhập chiều cao của An (cm): "))
chieu_cao_Minh = float(input("Nhập chiều cao của Minh (cm): "))
chieu_cao_Lan = float(input("Nhập chiều cao của Lan (cm): "))

# Xử lý so sánh
if chieu_cao_An > chieu_cao_Minh and chieu_cao_An > chieu_cao_Lan:
    print("An là người cao nhất.")
elif chieu_cao_Minh > chieu_cao_An and chieu_cao_Minh > chieu_cao_Lan:
    print("Minh là người cao nhất.")
elif chieu_cao_Lan > chieu_cao_An and chieu_cao_Lan > chieu_cao_Minh:
    print("Lan là người cao nhất.")
else:
    print("Có hai hoặc nhiều bạn có chiều cao bằng nhau cao nhất.")