class ClassTest:
    static = "Hello World!"
    
    def __init__(self, state):
        self.state = state
    
    def print_class_variable(self):
        print(self.static)
    
    @classmethod   
    def mod_class_variable(cls):
        cls.static = "Anything"

obj_1 = ClassTest(True)
obj_2 = ClassTest(True)

# Before
print(obj_1.static)
print(obj_2.static)
print(ClassTest.static)

obj_1.mod_class_variable()

# After
print(obj_1.static)
print(obj_2.static)
print(ClassTest.static)

