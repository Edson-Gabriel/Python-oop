class Artist:
    def __init__(self, type_artist : str):
        self.type_artist = type_artist

    def perform_a_show(self):
        print(f"The {self.type_artist} is performing his show.")
    
class Circus:
    def show(self, artist : Artist):
        print("The circus has opened!")
        artist.perform_a_show()
        print("The audience applauded!")
        
        
circus = Circus()
magic = Artist("magic")
circus.show(magic)