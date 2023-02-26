class Gyak01:
    def __init__(self, name) -> None:
        self.koszono_szoveg = "Üdv"
        self.name = name
    
    def say_something(self):
        szoveg = str(self.koszono_szoveg + " " + self.name)

        return szoveg
