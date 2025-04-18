# Viết một chương trình để tính tổng của tất cả các số chẵn trong một List.
def sum_even_numbers(numbers):
    # Khởi tạo biến tổng
    total = 0
    # Duyệt qua từng số trong danh sách
    for number in numbers:
        # Kiểm tra nếu số là chẵn
        if number % 2 == 0:
            # Cộng số chẵn vào tổng
            total += number
    return total
# Nhập danh sách số từ người dùng
input_numbers = input("Nhập các số cách nhau bởi dấu phẩy: ")
# Chuyển đổi chuỗi nhập vào thành danh sách số nguyên
numbers_list = [int(num) for num in input_numbers.split(",")]
# Tính tổng các số chẵn trong danh sách
even_sum = sum_even_numbers(numbers_list)
# In ra tổng các số chẵn
print("Tổng các số chẵn trong danh sách là:", even_sum)