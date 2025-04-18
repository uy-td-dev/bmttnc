#  Viết chương trình để truy cập các phần tử đầu tiên và cuối cùng trong một Tuple.
def access_first_last_elements(tup):
    # Truy cập phần tử đầu tiên và cuối cùng trong Tuple
    first_element = tup[0]
    last_element = tup[-1]
    return first_element, last_element
# Ví dụ sử dụng
my_tuple = (1, 2, 3, 4, 5)
first_element, last_element = access_first_last_elements(my_tuple)
print("Tuple ban đầu:", my_tuple)
print("Phần tử đầu tiên:", first_element)
print("Phần tử cuối cùng:", last_element)
# Nhập Tuple từ bàn phím    
input_tuple = tuple(map(int, input("Nhập Tuple các số nguyên cách nhau bởi dấu phẩy: ").split(',')))
first_element, last_element = access_first_last_elements(input_tuple)
print("Tuple nhập vào:", input_tuple)
print("Phần tử đầu tiên:", first_element)
print("Phần tử cuối cùng:", last_element)