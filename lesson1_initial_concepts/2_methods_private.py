class CellPhone:
    def __init__(self, brand, model, number, password):
        self.brand = brand
        self.model = model
        self.number = number
        self.__password = password
        self.power = False
        
    def power_on_off(self):
        if self.power:
            self.power = False
            return "Power OFF"
        else:
            self.power = True
            return "Power ON"
    
    def unlock(self, insert_password):
        if insert_password == self.__password:
            return "Phone unlocked"
        else:
            return "Incorrect password"
        
phone_1 = CellPhone(
    input("Brand: "),
    input("Model: "),
    input("Number: "),
    input("Password: ")
)

print(phone_1.power_on_off())

print(phone_1.unlock(input("Password: ")))
