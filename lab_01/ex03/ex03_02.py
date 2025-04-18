#  Viết chương trình để đảo ngược vị trí của các phần tử trong một danh sách.
def reverse_list(lst):
    # Sử dụng slicing để đảo ngược danh sách
    return lst[::-1]
# Ví dụ sử dụng
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print("Danh sách ban đầu:", my_list)
print("Danh sách sau khi đảo ngược:", reversed_list)
input_list = list(map(int, input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: ").split(',')))
reversed_input_list = reverse_list(input_list)
print("Danh sách sau khi đảo ngược:", reversed_input_list)