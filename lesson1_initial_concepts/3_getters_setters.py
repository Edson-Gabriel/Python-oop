class ClassTest:
    def __init__(self) -> None:
        # self_value = None # it is an incorret form
        self.__value = None
        
    def setter_value(self, value : int) -> None:
        self.__value = value
        
    def getter_value(self) -> int:
        return self.__value
    

my_class = ClassTest()
# my_class.value = 3 # Incorrect encapsulation

my_class.setter_value(50)
value = my_class.getter_value()
print(value)


# class ClassTest:
#     def __init__(self) -> None:
#         self.__value = None
        
#     def setter_value(self, value : int) -> None:
#         self.__value = value
    
#     @property        
#     def getter_value(self) -> int:
#         return self.__value
    

# my_class = ClassTest()

# my_class.setter_value(50)
# print(my_class.getter_value)