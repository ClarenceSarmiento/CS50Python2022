class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        added_cookie = self.size + n
        if added_cookie > self.capacity:
            raise ValueError("Deposit Error: Exceeded Cookie Jar's Capacity!")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw Error: Not Enough Cookie!")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Invalid Error: Negative Capacity!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Invalid Error: Full Capacity!")
        self._size = size

def main():
    jar = Jar()
    jar.deposit(6)
    print(jar)
    jar.withdraw(5)
    print(jar)
    jar.deposit(10)
    print(jar)

if __name__ == "__main__":
    main()