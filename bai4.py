def hien_thi_danh_sach(nhan_viens):
    print("=== DANH SÁCH NHÂN VIÊN ===")
    for nhan_vien in nhan_viens:
        print(f"Mã nhân viên: {nhan_vien['ma_nv']}")
        print(f"Tên nhân viên: {nhan_vien['ten_nv']}")
    print()

def tim_kiem_theo_ten(nhan_viens, tu_khoa):
    ket_qua = [nhan_vien for nhan_vien in nhan_viens if tu_khoa.lower() in nhan_vien['ten_nv'].lower()]
    print("=== KẾT QUẢ TÌM KIẾM ===")
    for nhan_vien in ket_qua:
        print(f"Mã nhân viên: {nhan_vien['ma_nv']}")
        print(f"Tên nhân viên: {nhan_vien['ten_nv']}")
    print()

def xoa_nhan_vien(nhan_viens, ma_nv_xoa):
    for nhan_vien in nhan_viens:
        if nhan_vien['ma_nv'] == ma_nv_xoa:
            nhan_viens.remove(nhan_vien)
            print("=== KẾT QUẢ SAU KHI XOÁ ===")
            hien_thi_danh_sach(nhan_viens)
            return
    print("Không có nhân viên này.")

def them_nhan_vien(nhan_viens, ma_nv, ten_nv):
    nhan_vien_moi = {
        "ma_nv": ma_nv,
        "ten_nv": ten_nv
    }
    nhan_viens.append(nhan_vien_moi)
    print("=== KẾT QUẢ SAU KHI THÊM ===")
    hien_thi_danh_sach(nhan_viens)


# Danh sách nhân viên ban đầu
employees = [
    {"ma_nv": 1, "ten_nv": "Nguyễn Văn A"},
    {"ma_nv": 2, "ten_nv": "Dương Trọng C"},
    {"ma_nv": 3, "ten_nv": "Nguyễn Thanh N"}
]
while True:
    print("\nChương trình xử lý từ điển Anh - Việt:")
    print("1. Hiển thị từ điển")
    print("2. Tìm kiếm từ")
    print("3. Xoá từ")
    print("4. Thêm từ mới")
    print("5. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn (1-5): ")

    if lua_chon == '1':
        # a) Hiển thị danh sách nhân viên
        hien_thi_danh_sach(employees)
    elif lua_chon == '2':
        # b) Tìm kiếm nhân viên theo tên
        tu_khoa_tim_kiem = input("Nhập từ khoá tìm kiếm: ")
        tim_kiem_theo_ten(employees, tu_khoa_tim_kiem)
    elif lua_chon == '3':
        # c) Xoá một nhân viên khỏi danh sách
        ma_nv_can_xoa = int(input("Nhập mã nhân viên muốn xoá: "))
        xoa_nhan_vien(employees, ma_nv_can_xoa)
    elif lua_chon == '4':
        # d) Thêm một nhân viên mới vào danh sách
        ma_nv_moi = int(input("Nhập mã nhân viên: "))
        ten_nv_moi = input("Nhập tên nhân viên: ")
        them_nhan_vien(employees, ma_nv_moi, ten_nv_moi)
    elif lua_chon == '5':
        print("Chương trình kết thúc. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

    input("Nhấn Enter để tiếp tục...")
