#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = "Used"

    def get_size(self):
        return self._size
    
    def set_size(self, size_value):
        if not isinstance(size_value, int):
            print("size must be an integer")
        else:
            self._size = size_value
    
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

shoe = Shoe("Adidas", 9)
shoe.size = "23"
print(f"{shoe.brand}, {shoe.size}")
print(shoe.condition)
shoe.cobble()
print(shoe.condition)