class ClassTest:
    static = "Hello World!"
    
    def __init__(self, state):
        self.state = state
        

obj_1 = ClassTest(True)
obj_2 = ClassTest(True)

ClassTest.static = "Hey!"
obj_1.static = "Python!!"

print(obj_1.static)
print(obj_2.static)
print(ClassTest.static)