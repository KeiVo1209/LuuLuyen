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

#Tính tổng các pt ở vị trí chẵn hàng i, với i nhập từ bán phím
m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
A =[[int(input()) for j in range(n)] for i in range(m)]
print(A)

s=0#biến  tổng
i=int(input("nhap i:"))
i-=1#i=i trước đó -
for j in range(n):#duyệt các pt theo đường ngang trong 1 hàng(cột)
       if j%2==0:#kiểm tra vị trí j chẵn->cộng giá trị vào biến 
           s+=A[i][j]
print("tong các phan tu o vi tri chan cua hang",i+1,"la", s)
 
#Tính tổng pt âm và k âm ở hàng i của a
m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
A =[[int(input()) for j in range(n)] for i in range(m)]
print(A)
ta=0
td=0
i=int(input("nhap i:"))
i-=1#i=i trước đó -1
for j in range(n):#duyệt các pt theo đường ngang trong 1 hàng(cột)
       if A[i][j]<0: #kiểm tra vị trí j chẵn->cộng giá trị vào biến 
           ta+=A[i][j]
       else: td+=A[i][j]
print("tong các phan tu am cua hang",i+1,"la", ta)
print("tong các phan tu duong cua hang",i+1,"la", td)

#tìm vị trí k trong mảng 2 chiều
m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
A =[[int(input()) for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        print(A[i][j], end=" ")
    print() 
k=int(input("nhap so k"))
for i in range (m):
   for j in range(n):
       if A[i][j]==k: 
          print('Tim thay k=',k,'o hang',i+1,'cot',j+1)


       



       



       

        
