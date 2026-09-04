print("======Dự án chuyến đi chơi======")

ten = input("nhập tên chuyến đi: ")
so_nguoi= int(input("Nhập số người: "))
so_ngay= int(input("nhập số ngày: "))

tien_xe = float(input("nhập tiền xe: "))
tien_khach_san = float(input("nhập tiền khách sạn: "))
tien_an = float(input("nhập tiền ăn: "))

khach_san = tien_khach_san * so_ngay
an = tien_an * so_nguoi * so_ngay
tong = tien_xe + khach_san + an

print("======Kết quả======")
print("Chuyến đi:", ten)
print("tiền xe:", tien_xe)
print("tieenf khách sạn:", khach_san)
print("tiền awn :", an)
print("TỔNG CHI PHÍ:", tong)