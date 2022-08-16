class Calculator:
    def __init__(self, roman_string):
        self.roman_string = roman_string

    def calculate_roman(roman_string):
        total = 0
        for char in roman_string:
            if char == "I":
                total += 1
            if char == "V":
                total += 5
            if char == "X":
                total += 10
            if char == "L":
                total += 50
            if char == "C":
                total += 100
            if char == "D":
                total += 500
            if char == "M":
                total += 1000

        return total

