# Hãy phát triển một chương trình để nhập vào một chuỗi các số nhị phân
# với 4 chữ số, phân cách bằng dấu phẩy. Chương trình sẽ kiểm tra từng số để xác
# định xem chúng có chia hết cho 5 hay không, sau đó in ra những số thỏa mãn điều
# kiện này, cũng được phân tách bằng dấu phẩy. Ví dụ, nếu đầu vào là: ‘0100’ , ‘0011’ ‘1010’ , ,‘1001’, thì kết quả đầu ra sẽ là: ‘1010’.
def check_divisible_by_5(binary_numbers):
    # Chia tách chuỗi đầu vào thành danh sách các số nhị phân
    binary_list = binary_numbers.split(",")
    
    # Tạo danh sách để lưu các số chia hết cho 5
    divisible_by_5 = []
    
    # Duyệt qua từng số nhị phân trong danh sách
    for binary in binary_list:
        # Chuyển đổi số nhị phân thành số thập phân
        decimal_number = int(binary, 2)
        
        # Kiểm tra xem số thập phân có chia hết cho 5 hay không
        if decimal_number % 5 == 0:
            divisible_by_5.append(binary)
    
    # Trả về danh sách các số chia hết cho 5, được nối bằng dấu phẩy
    return ",".join(divisible_by_5)
# Nhập vào chuỗi các số nhị phân
binary_numbers = input("Nhập vào chuỗi các số nhị phân (phân cách bằng dấu phẩy): ")
# Gọi hàm và in kết quả
result = check_divisible_by_5(binary_numbers)
print("Các số nhị phân chia hết cho 5 là:", result)