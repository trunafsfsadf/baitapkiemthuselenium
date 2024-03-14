# Nhập số nguyên n từ người dùng và kiểm tra điều kiện
while True:
    n = int(input("Nhập số nguyên n (n > 0): "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")

# Khởi tạo mảng a với n phần tử
a = [0] * n

# Nhập dãy số từ người dùng
for i in range(n):
    a[i] = int(input(f"a[{i}] = "))

# Tìm số dương lớn nhất và số âm bé nhất
max_positive = None
min_negative = None

for num in a:
    if num > 0:
        if max_positive is None or num > max_positive:
            max_positive = num
    elif num < 0:
        if min_negative is None or num < min_negative:
            min_negative = num

# Xuất kết quả
print("Số dương lớn nhất:", "*" if max_positive is None else max_positive)
print("Số âm bé nhất:", "*" if min_negative is None else min_negative)
