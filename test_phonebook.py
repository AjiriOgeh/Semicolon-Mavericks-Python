from unittest import TestCase
import phonebook


class Test(TestCase):

    def test_add_contact_to_phonebook(self):
        phonebook.add_contact_to_phonebook("bola", "Bola street", "08123456789", "bola@yahoo.com")

        self.assertEqual(len(phonebook.phonebook), 1)
        self.assertEqual(phonebook.phonebook[0]["name"], "bola")

    def test_delete_contact_in_phonebook(self):
        phonebook.add_contact_to_phonebook("bola", "Bola street", "08123456789", "bola@yahoo.com")
        phonebook.add_contact_to_phonebook("dayo", "Bola street", "08123456789", "bola@yahoo.com")
        phonebook.delete_contact_in_phonebook("bola")
        self.assertEqual(len(phonebook.phonebook), 1)

    def test_search_for_contact_in_phonebook(self):
        phonebook.add_contact_to_phonebook("bola", "Bola street", "08123456789", "bola@yahoo.com")
        phonebook.search_for_contact_in_phonebook("bola")
        self.assertEqual("""name :  bola
address :  Bola street
number :  08123456789
email :  bola@yahoo.com""")

    def test_display_menu(self):
        self.assertEqual("""Phonebook Menu
1.Add contact
2.Delete contact
3.Edit contact
4.Search contact
5.View existing contacts   
6.Exit""", phonebook.display_menu())

    def test_view_contact_in_phonebook(self):
        phonebook.add_contact_to_phonebook("bola", "Bola street", "08123456789", "bola@yahoo.com")
        phonebook.view_contact_in_phonebook()
        self.assertEqual("""name :  bola
        address :  Bola street
        number :  08123456789
        email :  bola@yahoo.com""", phonebook.view_contact_in_phonebook())
