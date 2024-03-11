import unittest

from Account.exception.invalid_capacity_error import InvalidCapacityError
from Account.exception.invalid_pin_error import InvalidPinError
from Gun.Gun import Gun


class TestGun(unittest.TestCase):
    def setUp(self):
        self.gun = Gun(capacity=8, pin="1234")

    def test_that_gun_can_be_loaded(self):
        self.gun.load(5, "1234")
        self.assertEqual(self.gun.bullets, 5)

    def test_shooting(self):
        self.gun.load(6, "1234")
        self.gun.shoot("1234")
        self.assertEqual(self.gun.bullets, 5)

    def test_that_gun_is_empty(self):
        self.gun.load(0, "1234")
        self.gun.shoot("1234")
        self.assertEqual(self.gun.bullets, 0)

    def test_check_bullets(self):
        self.gun.load(5, "1234")
        self.assertEqual(self.gun.check_bullets("1234"), 5)

    def test_shoot_with_incorrect_pin_raises_invalid_pin_error(self):
        self.gun.load(6, "1234")
        self.gun.shoot("4321")
        self.assertRaises(InvalidPinError)

    def test_shoot_more_than_capacity_raises_invalid_capacity_error(self):
        self.gun.load(10, "1234")
        self.assertRaises(InvalidCapacityError)
