#đếm số lượng pt chẵn
m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
A =[[int(input()) for j in range(n)] for i in range(m)]
#xuất mảng 2 chiều cách 1( theo thứ tự bảng)
for i in range(m):
    for j in range(n):
        print(A[i][j], end=" ")
    print() 
#xuất mảng 2 chiều cách 2
print(A)
s=0#tạo biến đếm
for i in range(m):
    for j in range(n):#2 vòng for 'lồng nhau' duyệt các pt trong mảng 2 chiều
        if A[i][j]%2==0:
            s+=1
print("so luong cac so chan la", s) #xuất biến đếm
#tính tổng các lẻ có trong mảng 2 chiều 
m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
A =[[int(input()) for j in range(n)] for i in range(m)]
print(A)
s=0
for i in range(m):
    for j in range(n):#duyệt các pt trong mảng 2 chiều
       if A[i][j]%2==1:#nếu A[i][j] là số lẻ( chia cho 2 dư 1)
           s+=A[i][j]
print("tong các số lẻ la", s)
        
