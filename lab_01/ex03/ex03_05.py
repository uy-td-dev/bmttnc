# Viết chương trình để đếm số lần xuất hiện của mỗi phần tử trong một List và lưu kết quả vào một Dictionary.
def count_elements(lst):
    # Sử dụng Dictionary để đếm số lần xuất hiện của mỗi phần tử
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count
# Ví dụ sử dụng
my_list = [1, 2, 3, 1, 2, 1]
element_count = count_elements(my_list)
print("Danh sách ban đầu:", my_list)
print("Số lần xuất hiện của mỗi phần tử:", element_count)
# Nhập danh sách từ bàn phím
input_list = list(input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: ").split(','))
element_count_input = count_elements(input_list)
print("Danh sách nhập vào:", input_list)
print("Số lần xuất hiện của mỗi phần tử:", element_count_input)