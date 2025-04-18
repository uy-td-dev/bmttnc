# Viết chương trình để xóa một phần tử từ Dictionary theo key đã cho.
def remove_element_by_key(dct, key):
    # Xóa phần tử theo key
    if key in dct:
        del dct[key]
    return dct
# Ví dụ sử dụng
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
print("Dictionary ban đầu:", my_dict)
# Xóa phần tử theo key
updated_dict = remove_element_by_key(my_dict, key_to_remove)
print("Dictionary sau khi xóa phần tử theo key '{}':".format(key_to_remove), updated_dict)
