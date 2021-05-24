"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """Makes a new generator 
            creates two variables 
            self.start stores a original start point for reference 
            self.unique is the variable used to generate next sequential number
            self.unique is subtracted by one so that it starts at original starting point after being incremented"""
        self.start = start
        self.unique = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"
    
    def generate(self):
        """Takes unique variable and increments it by one"""
        self.unique += 1
        return self.unique

    def reset(self):
        """resets the unique starting point to original starting point"""
        self.unique = self.start - 1

