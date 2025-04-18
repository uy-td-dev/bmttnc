# Xây dựng một chương trình nhằm nhập số giờ làm việc hàng tuần của
# nhân viên và mức lương theo giờ tiêu chuẩn. Từ đó, thực hiện tính toán số tiền
# thực nhận của nhân viên. Cần lưu ý rằng số giờ tiêu chuẩn mỗi tuần là 44 giờ, và
# mỗi giờ làm thêm sẽ được trả 150% so với mức lương theo giờ tiêu chuẩn
so = float(input("Nhập số giờ làm việc hàng tuần: "))
luong = float(input("Nhập mức lương theo giờ tiêu chuẩn: "))
# Tính toán số tiền thực nhận của nhân viên
if so <= 44:
    tien = so * luong
else:
    tien = 44 * luong + (so - 44) * luong * 1.5
# In ra số tiền thực nhận của nhân viên
print("Số tiền thực nhận của nhân viên là:", tien)