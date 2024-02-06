from unittest import TestCase
import phonebook


class Test(TestCase):

    def test_add_contact_to_phonebook(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        self.assertEqual(len(phonebook.phonebook), 1)
        self.assertEqual(phonebook.phonebook[0]["name"], "ade")

    def test_add_contact_to_phonebook_two_contacts(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        phonebook.add_contact_to_phonebook("bola", "Bola Street", "08123456789", "bola@yahoo.com")
        self.assertEqual(len(phonebook.phonebook), 2)
        self.assertEqual(phonebook.phonebook[0]["name"], "ade")
        self.assertEqual(phonebook.phonebook[1]["name"], "bola")

    def test_delete_contact_in_phonebook(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        phonebook.delete_contact_in_phonebook("ade")
        self.assertEqual(len(phonebook.phonebook), 0)

    def test_delete_contact_in_phonebook_contact_does_not_exist(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        phonebook.delete_contact_in_phonebook("bola")
        self.assertEqual("bola is not listed in your contacts", phonebook.delete_contact_in_phonebook("bola"))

    def test_search_for_contact_in_phonebook(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        self.assertEqual("ade contact information", phonebook.search_for_contact_in_phonebook("ade"))

    def test_search_for_contact_in_phonebook_contact_does_not_exist(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        self.assertEqual("bola is not listed in your contacts", phonebook.search_for_contact_in_phonebook("bola"))

    def test_view_contact_in_phonebook(self):
        phonebook.phonebook.clear()
        phonebook.add_contact_to_phonebook("ade", "Ade Street", "09123456789", "ade@yahoo.com")
        self.assertEqual([{'name': 'ade', 'address': 'Ade Street', 'number': '09123456789', 'email': 'ade@yahoo.com'}], phonebook.view_contact_in_phonebook())
