from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateId(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateId()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTb = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svId,name,sex,major,diemTb)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self,id):
        sv: SinhVien = self.findById(id)
        if sv == None:
            print("Khong tim thay sinh vien co id = ",id)
            return
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTb = float(input("Nhap diem trung binh sinh vien: "))
        sv._name = name
        sv._sex = sex
        sv._major = major
        sv._diemTb = diemTb
        self.xepLoaiHocLuc(sv)
        print("Cap nhat sinh vien thanh cong")
    
    def sortById(self):
        self.listSinhVien.sort(key=lambda sv: sv._id,reverse=False)
        print("Sap xep sinh vien thanh cong")
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name,reverse=False)
        print("Sap xep sinh vien thanh cong")
    
    def sortByDiemTb(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTb,reverse=False)
        print("Sap xep sinh vien thanh cong")
    
    def findById(self,id):
        for sv in self.listSinhVien:
            if sv._id == id:
                return sv
        return None
    
    def findByName(self,name):
        result = []
        for sv in self.listSinhVien:
            if sv._name == name:
                result.append(sv)
        return result
    
    def deleteById(self,id):
        sv: SinhVien = self.findById(id)
        if sv == None:
            print("Khong tim thay sinh vien co id = ",id)
            return False
        self.listSinhVien.remove(sv)
        print("Xoa sinh vien thanh cong")
        return True
    
    def xepLoaiHocLuc(self,sv: SinhVien):
        if sv._diemTb >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTb >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTb >= 5:
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"
    
    def showList(self):
        for sv in self.listSinhVien:
            print("--------------------------------------------------")
            print(sv)
            print("ID: ",sv._id)
            print("Ten: ",sv._name)
            print("gioi tinh:",sv._sex)
            print("nganh hoc:",sv._major)
            print("diem trung binh:",sv._diemTb)
            print("hoc luc:",sv._hocLuc)
            print("--------------------------------------------------")
            print("\n")
    
    def getListSinhVien(self):
        return self.listSinhVien
    