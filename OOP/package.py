class Package():
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address}, Praha má hmotnost {self.weight} kg je ve stavu {self.state}"

address = "Korunni 23"
weight = 3
state = "nedorucen"

balik = Package(address, weight, state)


print(balik)