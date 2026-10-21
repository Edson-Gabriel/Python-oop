class Switch:
    def __init__(self, room : str):
        self.room = room
        
    def on(self) -> None:
        print(f"Light on in the {self.room}.")
        
    def off(self) -> None:
        print(f"Light off in the {self.room}.")
        
class Person:
    def ligth_on(self, switch : Switch) -> None:
        switch.on()
    
    def ligth_off(self, switch : Switch) -> None:
        switch.off()
        
    def sleep(self) -> None:
        print("The person went to bed")
        

gabriel = Person()
switch_bedroom = Switch("Bedroom")
gabriel.ligth_on(switch_bedroom)