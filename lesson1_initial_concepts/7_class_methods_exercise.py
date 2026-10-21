class Store:
    rate = 0
    
    def __init__(self, value):
        self.value_product_gross = value
        
    def calculate_product(self):
        prize_product = self.value_product_gross + ((self.rate*self.value_product_gross)/100) if self.rate >= 0 else self.value_product_gross
        print(f"R${prize_product:.2f}")
    
    @classmethod        
    def edit_rate_product(cls, new_rate):
        cls.rate = new_rate 
        

product_1 = Store(
    float(input("What gross value of the product? R$"))
)

product_1.calculate_product() #before

product_1.edit_rate_product(10)

product_1.calculate_product() #after