import unittest
from unittest.mock import patch
from Src.Controllers.ClientController import ClientController
from Src.Class.Client import Client
import Src.GlobalVariables.GlobalVariables as gv

class TestClientController(unittest.TestCase):
    def setUp(self):
        self.cc = ClientController()
        gv.client_list = []

    @patch("Src.Controllers.ClientController.APIController.write_client_on_csv")
    @patch("Src.Controllers.ClientController.messagebox.showinfo")

    def test_create_client_success(self, mock_warning, mock_write):
        self.cc.create_client("1",
                              "Mario",
                              "Rossi",
                              "abc@def.com",
                              "Via di qui 10",
                              "12345",
                              "1234567890")
        self.assertEqual(len(gv.client_list), 1)
        client = gv.client_list[0]
        self.assertEqual(client.FirstName, "Mario")
        self.assertEqual(client.LastName, "Rossi")
        mock_warning.assert_not_called()
        mock_write.assert_called_once()

if __name__ == "__main__":
    unittest.main()