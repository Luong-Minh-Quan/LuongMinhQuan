
num1,num2,num3,num4 = eval(input("Nhập số :"))
max_num = num1 
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4
print("Số lớn nhất là:", max_num)