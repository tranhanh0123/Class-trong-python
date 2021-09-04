
# class hcn:
    ## phương thức khởi tạo
    ## self : nghĩa là chính bản thân nó.
    ## cd,cr : là thuộc tính
#     def __init__(self,cd,cr):
#         self.cd = cd
#         self.cr = cr
#     #hàm lấy ra chiều dài và chiều rộng hcn hay còn gọi là phương thức hay gọi là hàm của lớp cũng dc.
#     def show(self):
#         self.cd
#         self.cr
#     def chuvi(self):
#         return(self.cd+self.cr)*2
#     def dientich(self):
#         return self.cd*self.cr
# #đưa chiều dài và chiều rộng vào qua class tổng
# hcn1 = hcn(56,12)
# #gán hcn1 bằng chiều dài và chiều rộng phía trên
# hcn1.show()
# print("Chu vi hcn là : ",hcn1.chuvi())
# print("diện tích hcn là : ",hcn1.dientich())






# Lớp con và tính kế thừa . Hình bình hành là trường hợp con của tứ giác.

# class tu_giac():
#     def __init__(self,a,b,c,d):
#         self.a = a 
#         self.b = b
#         self.c = c
#         self.d = d
#     def chuvi(self):
#         return self.a+self.b+self.c+self.d
# class hinh_binh_hanh(tu_giac):
#     pass
# hcn = tu_giac(5,8,6,9)
# print("chu vi hcn là: ",hcn.chuvi())
# hbh = hinh_binh_hanh(5,8,9,4)
# print("chu vi hình bình hành là : ",hbh.chuvi())


