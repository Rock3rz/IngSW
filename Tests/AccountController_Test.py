import unittest
from unittest.mock import patch
from Src.Controllers.AccountController import AccountController
from Src.Class.User import User
import Src.GlobalVariables.GlobalVariables as gv

class TestAccountController(unittest.TestCase):
    def setUp(self):
        self.ac = AccountController()
        gv.user_list = []
        genericUser = User(
            user_id = "1",
            email = "a@b.it",
            first_name = "Mario",
            username = "m",
            is_admin = False,
            last_name = "Rossi",
            password = "12345"
        )

        gv.user_list.append(genericUser)

    @patch("Src.Controllers.AccountController.messagebox.showwarning")
    def test_login_user_not_found(self,mock_warning):
        gv.canEnter = False
        self.ac.login("m", "123")
        mock_warning.assert_called_once()
        self.assertFalse(gv.canEnter)

    def test_login_user_found(self):
        gv.canEnter = False
        self.ac.login("m", "12345")
        self.assertTrue(gv.canEnter)

    @patch("Src.Controllers.AccountController.messagebox.showwarning")
    def test_create_user_fail_missing_field(self, mock_warning):
        self.ac.create_user(
            name = "Mario",
            last_name= "Cifeca",
            email= "a@b.virgilio.it",
            username= "",
            password = "123",
            is_admin = False
        )
        mock_warning.assert_called_once()
        self.assertEqual(len(gv.user_list), 1)

    @patch("Src.Controllers.AccountController.messagebox.showwarning")
    def test_create_user_duplicate(self, mock_warning):
        self.ac.create_user(
            name = "Mario",
            last_name= "Rossi",
            email= "a@b.it",
            username= "m",
            password= "12345",
            is_admin= False
        )
        mock_warning.assert_called_once()
        self.assertEqual(len(gv.user_list), 1)

    @patch("Src.Controllers.AccountController.APIController.write_user_on_csv")
    def test_create_user_success(self, mock_write):
        self.ac.create_user(
            name="Mario",
            last_name="Cifeca",
            email="a@b.virgilio.it",
            username="ma",
            password="123",
            is_admin=False
        )
        mock_write.assert_called_once()
        self.assertEqual(len(gv.user_list), 2)
        self.assertEqual(gv.user_list[1].firstName, "Mario")
        self.assertEqual(gv.user_list[1].LastName, "Cifeca")

if __name__ == '__main__':
    unittest.main()