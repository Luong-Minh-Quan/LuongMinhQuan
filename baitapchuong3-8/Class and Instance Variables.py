class Dog:
    tricks = [] #xóa dòng này đi
    kind = 'canine'
    def __init__(self, name):
        self.name = name  
        #self.tricks = [] dòng này để tạo một danh sách mới cho mỗi chú chó
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) #print(d.tricks)
                #['roll over']
                #print(e.tricks)
                #['play dead']
print(d.kind)                
print(e.kind)                  
print(d.name)               
print(e.name)   