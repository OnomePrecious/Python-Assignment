import unittest

from Gun import Gun


class MyTestCase(unittest.TestCase):

    def test_that_gun_can_be_loaded(self):
        my_gun: Gun()
        self.my_gun.ammo_count(10)
        self.assertEqual(self.my_gun.ammo_count, 10)

