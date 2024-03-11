from Account.exception.invalid_capacity_error import InvalidCapacityError
from Account.exception.invalid_pin_error import InvalidPinError


class Gun:
    def __init__(self, capacity, pin):
        self.capacity = capacity
        self.pin = pin
        self.bullets = 0

    def pin(self):
        self.pin = self.pin
        if self.pin == self.pin:
            return self.pin

    def load(self, number_of_bullets, pin):
        self.pin = pin
        if number_of_bullets <= self.capacity:
            self.bullets += number_of_bullets
            return self.bullets
        else:
            return "Not enough bullets"

    def shoot(self, pin):
        self.pin = pin
        if self.bullets > 0:
            self.bullets -= 1
            return "kpa"
        else:
            return "Out of bullet"

    def check_bullets(self, the_pin):
        if the_pin != self.pin:
            raise InvalidPinError("Incorrect pin")
        return self.bullets

    def set_pin(self, my_pin):
        self.pin = my_pin
        return self.pin

    def validate_pin(self, the_pin):
        if the_pin == self.pin:
            return self.pin
        else:
            raise InvalidPinError

    def validate_capacity(self, the_capacity):
        if the_capacity == self.capacity:
            return self.capacity
        else:
            raise InvalidCapacityError
