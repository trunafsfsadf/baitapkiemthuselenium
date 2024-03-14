dictionary = {}

def them_tu_moi():
    tu = input("Nhập từ tiếng Anh mới: ")
    nghia = input("Nhập nghĩa tiếng Việt của từ: ")
    dictionary[tu] = nghia
    print("Đã thêm từ mới vào từ điển.")

def hien_thi_tu_dien():
    print("Từ điển hiện tại:")
    for tu, nghia in dictionary.items():
        print(f"{tu}: {nghia}")
    print(f"Tổng số từ trong từ điển: {len(dictionary)}")

def tim_kiem_tu():
    tu_can_tim = input("Nhập từ tiếng Anh cần tìm: ")
    if tu_can_tim in dictionary:
        print(f"Tìm thấy từ '{tu_can_tim}': {dictionary[tu_can_tim]}")
    else:
        print(f"Không tìm thấy từ '{tu_can_tim}' trong từ điển.")

def xoa_tu():
    tu_can_xoa = input("Nhập từ tiếng Anh cần xóa: ")
    if tu_can_xoa in dictionary:
        del dictionary[tu_can_xoa]
        print(f"Đã xóa từ '{tu_can_xoa}' khỏi từ điển.")
    else:
        print(f"Không tìm thấy từ '{tu_can_xoa}' trong từ điển.")


while True:
    print("\nChương trình xử lý từ điển Anh - Việt:")
    print("1. Thêm từ mới")
    print("2. Hiển thị từ điển")
    print("3. Tìm kiếm từ")
    print("4. Xoá từ")
    print("5. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn (1-5): ")

    if lua_chon == '1':
        them_tu_moi()
    elif lua_chon == '2':
        hien_thi_tu_dien()
    elif lua_chon == '3':
        tim_kiem_tu()
    elif lua_chon == '4':
        xoa_tu()
    elif lua_chon == '5':
        print("Chương trình kết thúc. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
