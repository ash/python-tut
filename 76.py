class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no
 
roll_no = 12

x = Student(5)
y = Student(7)

print(x.roll_no) # 5
print(y.roll_no) # 7

print(roll_no) # just a global variable 12
