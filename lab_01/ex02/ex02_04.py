# Tạo một danh sách rỗng để lưu kết quả
results = []
# Duyệt qua tất cả các số trong đoạn từ 2000 đến 3000, kiêm tra xem số đó có chia hết cho 7 và không phải là bội số của 5 hay không
for i in range(2000, 3001):
    if i % 7 == 0 and i % 5 != 0:
        results.append(str(i))
# In kết quả
print(",".join(results))
