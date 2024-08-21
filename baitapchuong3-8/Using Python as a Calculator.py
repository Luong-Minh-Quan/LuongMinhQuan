print(2 + 2)
print(50 - 5*6)
print((50 - 5*6) / 4)
print(8 / 5)
print(17 / 3)
print(17 // 3)  
print(17 % 3) 
print(5 * 3 + 2)
print(5 ** 2)
print(2 ** 7)
width = 20
height = 5 * 9
print(width * height)
print(4 * 3.75 - 1)
print('spam eggs')
print("Paris rabbit got your back :)! Yay!")
print('1975')
print("doesn't")
print('doesn\'t')
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
print(s)
print('C:\some\name') 
print(r'C:\some\name')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(3 * 'un' + 'ium')
print('Py' 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
prefix = 'Py'
print(prefix + 'thon')
word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[4:])
print(word[-2:])
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[4:42])
print(word[42:])
print('J' + word[1:])
print(word[:2] + 'py')
s = 'supercalifragilisticexpialidocious'
print(len(s))
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares + [36, 49, 64, 81, 100])
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))
rgba.append("Alph")
print(rgb)
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba
print(correct_rgba)
print(rgba)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
i = 256*256
print('The value of i is', i)
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


