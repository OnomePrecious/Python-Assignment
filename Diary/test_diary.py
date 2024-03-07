import unittest

from Diary.diary import Diary


class MyTestCase(unittest.TestCase):
    def test_create_entry(self):
        my_diary = Diary("Precious", "1234")
        my_diary.create_entry("Had i known", "story of my life")
        self.assertEqual("new entry created", my_diary.create_entry("Had i known", "story of my life"))

    def test_that_i_can_create_two_entry(self):
        my_diary = Diary("Precious", "1234")
        my_diary.create_entry("The great mistake", "story of my life part 2")
        self.assertEqual("new entry created", my_diary.create_entry("Had i known", "story of my life"))
        my_diary.create_entry("I have to move on", "story of my life part 3")
        self.assertEqual("new entry created", my_diary.create_entry("Had i known", "story of my life"))

    def test_lock_diary(self):
        my_diary = Diary("Precious", "1234")
        my_diary.lock_diary()
        self.assertTrue(my_diary.locked)

    def test_unlock_diary(self):
        my_diary = Diary("Precious", "1234")
        my_diary.lock_diary()
        self.assertTrue(my_diary.locked)
        my_diary.unlock_diary()
        self.assertFalse(my_diary.locked)

    def test_delete_entry(self):
        my_diary = Diary("Precious", "1234")
        my_diary1 = my_diary.find_entry_by_id(1)
        message = my_diary.delete_entry(my_diary1)
        self.assertEqual(message, my_diary.delete_entry(1))

    def test_find_user_by_id(self):
        my_diary = Diary("Precious", "1234")
        my_diary1 = my_diary.find_entry_by_id(1)
        message = my_diary.find_entry_by_id(1)
        self.assertEqual(message, my_diary.find_entry_by_id(1))

    def test_update_entry(self):
        my_diary = Diary("Precious", "1234")
        my_diary.update_entry(1, "Had i known", "story of my life")
        self.assertEqual("entry updated successfully",
                         my_diary.update_entry(1, "I would not have fallen in love", "another story of my life"))


if __name__ == '__main__':
    unittest.main()
