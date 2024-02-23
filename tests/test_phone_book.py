import pytest

import phone_book.phone_book


class TestPhoneBook:

    def test_phonebook_can_add_contact(self):
        phone_book.phone_book.add_contact("precious", "070372787285")
        assert phone_book.phone_book.search_contact("precious") == "Phone number: 070372787285"

def test_phonebook_can_add_and_save_contact(self):
        phone_book.phone_book.add_contact("Precious", "08034576543")
        assert phone_book.phone_book