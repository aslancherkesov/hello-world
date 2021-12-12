from typing import ValuesView


class Sample_Class:
    def __init__(self, Name, Age, Height, Weight) -> None:
        self.Imya = Name
        self.Vozrast = Age
        self.Rost = Height
        self.Ves = Weight
Imya = "Aslan"
Vozrast = 35
Rost = 188
Ves = 88
User = Sample_Class(Imya, Vozrast, Rost, Ves)

print(User.Imya)
