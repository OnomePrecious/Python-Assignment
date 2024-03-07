class Gun:
    def __init__(self, pin):
        self._ammo_count = 0
        self._pin = pin

    def get_ammo_count(self):
        return self._ammo_count

    def pin(self):
        self.pin = self.pin
        if self._pin == self._pin:
            return self.pin

    def load(self, amount, pin):
        pin(pin)
        self._ammo_count += amount

     def shoot(self, pin):
        self.pin = pin
        if pin == pin:
            return self.pin

        if self._ammo_count > 0:
            return "kpa"
        else:
            return "Out of bullet"
