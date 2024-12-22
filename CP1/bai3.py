# Nhập năm từ người dùng
nam = int(input("Nhập năm: "))

# Kiểm tra điều kiện năm nhuận
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")