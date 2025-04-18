# Tạo một chương trình để nhập vào hai số X và Y; từ đó, xây dựng một
# mảng hai chiều. Giá trị của mỗi phần tử tại hàng i và cột j của mảng sẽ là i*j, với i
# chạy từ 0 đến X-1 và j từ 0 đến Y-1. Chẳng hạn, nếu X và Y được nhập là 3 và 5,
#thì kết quả sẽ là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]].
input_x = int(input("Nhập số X: "))
input_y = int(input("Nhập số Y: "))
array = []
for i in range(input_x):
    row = []
    for j in range(input_y):
        row.append(i * j)
    array.append(row)
print(array)