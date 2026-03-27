class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        amount = ""
        for _ in range(self.size):
            amount += "🍪"
        return f"{amount}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # Setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    # Getter
    @property
    def size(self):
        return self._size

    # Setter
    @size.setter
    def size(self, size):
        self._size = size
