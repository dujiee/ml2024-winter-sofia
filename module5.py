
class NumberTracker:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def find_index(self, x):
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1
