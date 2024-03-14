def hinh_chu_nhat(N):
    for i in range(N):
        print('*' * N)


def tam_giac_tang(N):
    for i in range(1, N + 1):
        print('*' * i)


def tam_giac_giam(N):
    for i in range(N, 0, -1):
        print('*' * i)


def tam_giac_vuong_giam(N):
    for i in range(N):
        print(' ' * i + '*' * (N - i))


# Nhập số nguyên N từ người dùng và kiểm tra điều kiện
while True:
    input_N = int(input("Nhập số nguyên N: "))
    if input_N > 0:
        break
    else:
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")

# Xuất các hình tương ứng với giá trị của N
print("\nHình chữ nhật:")
hinh_chu_nhat(input_N)

print("\nTam giác tăng:")
tam_giac_tang(input_N)

print("\nTam giác giảm:")
tam_giac_giam(input_N)

print("\nTam giác vuông giảm:")
tam_giac_vuong_giam(input_N)
