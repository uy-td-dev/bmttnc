#  Viết chương trình để tạo một Tuple từ một List nhập vào từ bàn phím.
def list_to_tuple(lst):
    # Chuyển đổi danh sách thành Tuple
    return tuple(lst)
# Ví dụ sử dụng
my_list = [1, 2, 3, 4, 5]
converted_tuple = list_to_tuple(my_list)
print("Danh sách ban đầu:", my_list)
print("Tuple sau khi chuyển đổi:", converted_tuple)
# Nhập danh sách từ bàn phím
input_list = list(map(int, input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: ").split(',')))
converted_input_tuple = list_to_tuple(input_list)
print("Tuple sau khi chuyển đổi:", converted_input_tuple)