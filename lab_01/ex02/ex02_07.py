#  Xây dựng một chương trình để nhận các chuỗi đầu vào là những dòng được nhập, sau đó chuyển đổi các dòng này thành chữ hoa và hiển thị kết quả lên màn hình.
print("Nhập các dòng văn bản (nhấn Enter để kết thúc):")
lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line.upper())
print("Các dòng văn bản đã chuyển đổi thành chữ hoa:")
for line in lines:
    print(line)
# Chương trình này sẽ yêu cầu người dùng nhập các dòng văn bản và chuyển đổi chúng thành chữ hoa