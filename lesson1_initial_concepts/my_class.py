from datetime import datetime


class Person:
    
    current_year = datetime.now().year
    
    def __init__(self,name, height, weight, year_of_birth):
        self.name = name
        self.height = height
        self.weight = weight
        self.year_of_birth = year_of_birth
        
    def calculate_bmi(self):
        bmi = self.weight / (self.height**2)
        if bmi < 18.5:
            classification = "Below the ideal range."
        elif bmi < 25:
            classification = "Ideal weight."
        elif bmi < 30:
            classification = "Overweight."
        elif bmi < 35:
            classification = "Grade I obesity."
        elif bmi < 40:
            classification = "Grade II (severe) obesity."
        else:
            classification = "Grade III (morbid) obesity."
        
        return bmi, classification
        
    def calculate_age(self):
        return self.current_year - self.year_of_birth
    
    def show_info(self):
        bmi, classification = self.calculate_bmi()
        age = self.calculate_age()
        
        return f"Hi {self.name}!\nYou turned or will turn {age}.\nYour bmi {bmi:.1f}. Classification: {classification}"
    

for i in range(3):
    print("-"*40)
    person = Person(
        input("what's your name? "),
        float(input("What is your height in M? ")),
        float(input("What is your weight in KG? ")),
        int(input("In which year were you born? "))
    )
    print("-"*40)
    print(person.show_info())
