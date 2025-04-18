# Viết hàm kiểm tra xem một số được nhập vào có phải là số nguyên tố hay không.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Nhập số từ người dùng
number = int(input("Nhập một số nguyên: "))
# Kiểm tra xem số có phải là số nguyên tố hay không
if is_prime(number):
    print(f"{number} là số nguyên tố.")
else:
    print(f"{number} không phải là số nguyên tố.")
