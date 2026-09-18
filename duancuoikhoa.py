print("====== DỰ ÁN CHUYẾN ĐI CHƠI ======")

ten = input("Nhập tên chuyến đi: ")

while True:
    try:
        so_nguoi = int(input("Nhập số người: "))

        if so_nguoi <= 0:
            print("Lỗi! Số người phải lớn hơn 0.")
        else:
            break

    except:
        print("Lỗi! Vui lòng nhập số.")


while True:
    try:
        so_ngay = int(input("Nhập số ngày: "))

        if so_ngay <= 0:
            print("Lỗi! Số ngày phải lớn hơn 0.")
        else:
            break

    except:
        print("Lỗi! Vui lòng nhập số.")


while True:
    try:
        tien_xe = float(input("Nhập tiền xe: "))

        if tien_xe < 0:
            print("Lỗi! Tiền không được nhỏ hơn 0.")
        else:
            break

    except:
        print("Lỗi! Vui lòng nhập số.")


while True:
    try:
        tien_khach_san = float(input("Nhập tiền khách sạn mỗi ngày: "))

        if tien_khach_san < 0:
            print("Lỗi! Tiền không được nhỏ hơn 0.")
        else:
            break

    except:
        print("Lỗi! Vui lòng nhập số.")


while True:
    try:
        tien_an = float(input("Nhập tiền ăn mỗi người mỗi ngày: "))

        if tien_an < 0:
            print("Lỗi! Tiền không được nhỏ hơn 0.")
        else:
            break

    except:
        print("Lỗi! Vui lòng nhập số.")


khach_san = tien_khach_san * so_ngay
an = tien_an * so_nguoi * so_ngay
tong = tien_xe + khach_san + an
chi_phi_moi_nguoi = tong / so_nguoi
chi_phi_moi_ngay = tong / so_ngay


print()
print("====== KẾT QUẢ ======")

print("Chuyến đi:", ten)
print("Số người:", so_nguoi)
print("Số ngày:", so_ngay)

print("----------------------")
print("Tiền xe:", tien_xe)
print("Tiền khách sạn:", khach_san)
print("Tiền ăn:", an)

print("----------------------")
print("TỔNG CHI PHÍ:", tong)
print("Chi phí mỗi người:", chi_phi_moi_nguoi)
print("Chi phí mỗi ngày:", chi_phi_moi_ngay)