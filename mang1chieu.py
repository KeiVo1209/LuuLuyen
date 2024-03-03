#Tống, tbc
S=0
n= int(input("nhap so phan tu: "))
luyen = [int(input()) for i in range(n)]
print(luyen)
for i in range (n):
   S+=luyen[i] #S=S+A[i]
print("Tong cua mang",S)
print("Trung binh cong",S/n)
#Tổng các pt chẵn
S=0
n= int(input("nhap so phan tu: "))
luyen = [int(input()) for i in range(n)]
print(luyen)
for i in range (n):
    if (luyen[i]%2==0): 
        S+=luyen[i]
print("tong cac pt chan", S)
#tổng các pt ở vị trí lẻ
S=0
n= int(input("nhap so phan tu:"))
luyen = [int(input()) for i in range(n)]
print(luyen)
for i in range (n):
    if i%2==1: 
        S+=luyen[i]
print("tong cac pt o vi tri le", S)
#xóa các ptu là số âm trong mảng
S=[]
n= int(input("nhap so phan tu:"))
luyen = [int(input()) for i in range(n)]
print(luyen)
for i in range (n):
    if (luyen[i]>=0):
        S.append(luyen[i])
print("xoa cac ptu am:",S)
#xóa pt âm cách 2
n= int(input("nhap so phan tu:"))
luyen = [int(input()) for i in range(n)]
print(luyen)
for i in range (n-1,-1,-1):
    if (luyen[i]<0):
        luyen.remove(luyen[i])
print("xoa cac ptu am:",luyen)
#tìm vị trí ptu lớn nhất trong mảng
n= int(input("nhap so phan tu:"))
luyen = [int(input()) for i in range(n)]
Max=max(luyen)
print(luyen)
for i in range (n):
    if (luyen[i]==Max):
       print(i)
