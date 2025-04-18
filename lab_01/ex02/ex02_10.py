#Viết một hàm nhận vào một chuỗi và trả về chuỗi đảo ngược của nó.
def reverse_string(s):
    return s[::-1]
# Nhập chuỗi từ người dùng
input_string = input("Nhập một chuỗi: ")
# Đảo ngược chuỗi
reversed_string = reverse_string(input_string)
# In ra chuỗi đảo ngược
print("Chuỗi đảo ngược là:", reversed_string)