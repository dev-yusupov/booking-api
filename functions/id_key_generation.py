from random import randint

class RandomID:
    """Class generates 6-digit numbers for ID of objects in models."""
    def generate_six_digit_id(self) -> int:
        number = ""
        for i in range(7):
            number += str(randint(0, 9))
        
        return int(number)