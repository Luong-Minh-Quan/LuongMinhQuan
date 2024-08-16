import math
a,b,c=eval(input("nhập các số nguyên dương:"))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình vô nghiệm")