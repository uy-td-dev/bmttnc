from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\n Chuong trinh quan ly sinh vien")
    print("*" * 50)
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim sinh vien")
    print("5. Sap xep sinh vien theo diem tb")
    print("6. Sap xep sinh theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("8. Thoat")
    print("*" * 50)
    choice = int(input("Nhap lua chon: "))
    if choice == 1:
        qlsv.nhapSinhVien()
    elif choice == 2:
        id = int(input("Nhap id sinh vien can cap nhat: "))
        qlsv.updateSinhVien(id)
    elif choice == 3:
        id = int(input("Nhap id sinh vien can xoa: "))
        qlsv.deleteById(id)
    elif choice == 4:
        id = int(input("Nhap id sinh vien can tim: "))
        sv = qlsv.findById(id)
        if sv != None:
            print(sv)
        else:
            print("Khong tim thay sinh vien co id = ",id)
    elif choice == 5:
        qlsv.sortByDiemTb()
        qlsv.showList()
    elif choice == 6:
        qlsv.sortByName()
    elif choice == 7:
        qlsv.showList()
    elif choice == 8:
        break
    else:
        print("Lua chon khong hop le")
