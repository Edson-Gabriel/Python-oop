class Phone:
    def __init__(self, model : str) -> None:
        self.model = model
        
    def send_msg(self, msg: str) -> None:
        print(f"Send messenger: {msg}")
        
    def open_emails(self) -> None:
        print("Open emails...")
    
    def open_youtube(self) -> None:
        print("Open YouTube...")

class People:
    def __init__(self, phone : Phone):
        self.__phone = phone
    
    def order_out_pizza(self):
        print("Pizza!")
        self.__phone.send_msg("Chess pizza")
        print("Wait for your order")
    
    def order_out_hamburger(self):
        print("Hamburger!")
        self.__phone.send_msg("Bacon burger")
        print("Wait for your order")
        
android = Phone("Samsung")
ios = Phone("Iphone")

gabriel = People(android)
yasmin = People(ios)

gabriel.order_out_hamburger()
print()
yasmin.order_out_pizza()