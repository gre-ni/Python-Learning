class Vault():
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."
    
    # Operator overload
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    

potter = Vault(12, 56, 90)
print(potter)

weasley = Vault(80, 5, 22)

total = potter + weasley # This is adjusted with operator override, otherwise would raise TypeError