class Gun:
    def __init__(self, name, caliber,  magazine):
        self._name = name
        self._caliber = caliber
        self._magazine = magazine
        self._ammo_count = 0

    def get_ammo_count(self):
        return self._ammo_count

    def load(self, amount):
        self._ammo_count += amount

    def shoot(self):
        if self._ammo_count > 0:
            return "kpa"
        else:
            if self._ammo_count < 0:
                return "Out of bullet"
