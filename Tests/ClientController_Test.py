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



    @patch("Src.Controllers.ClientController.messagebox.showwarning")
    def test_create_client_missing_field(self, mock_warning):
        # Arrange
        gv.client_list = []  # assicurati lista vuota

        # Act: FirstName mancante
        self.cc.create_client(
            "1",  # id
            "",  # FirstName mancante
            "Rossi",  # LastName
            "mario@rossi.com",  # Email
            "Milano",  # Address
            "20100",  # CAP
            "1234567890"  # Phone
        )

        # Assert
        self.assertEqual(len(gv.client_list), 0)  #nessun client aggiunto
        mock_warning.assert_called_once()  #warning mostrato


    @patch("Src.Controllers.ClientController.APIController.write_client_on_csv")
    @patch("Src.Controllers.ClientController.messagebox.showwarning")
    def test_create_client_duplicate(self, mock_warning, mock_write):
        gv.client_list = []
        gv.client_list.append(Client("Milano",  # city
            "mario@rossi.com",  # Email
            "Mario",  # FirstName
            "Rossi",  # LastName
            "1",  # id
            "1234567890",  # Phone
            "20100"  # CAP
            ))

        self.cc.create_client(
            next_id="1",
            name="Mario",
            last_name="Rossi",
            email="mario@rossi.com",
            address="Milano",
            cap="20100",
            phone_number="1234567890")
        self.assertEqual(len(gv.client_list), 1)
        mock_warning.assert_called_once()
        mock_write.assert_not_called()

    @patch("Src.Controllers.ClientController.APIController.write_client_on_csv")
    @patch("Src.Controllers.ClientController.messagebox.showwarning")
    def test_edit_client_info_success(self, mock_warning, mock_write):
        gv.client_list = []
        gv.client_list.append(Client("Milano",  # city
                                     "mario@rossi.com",  # Email
                                     "Mario",  # FirstName
                                     "Rossi",  # LastName
                                     "1",  # id
                                     "1234567890",  # Phone
                                     "20100"  # CAP
                                     ))
        gv.CurrentClient = gv.client_list[0]
        self.cc.edit_client_infos(
            name="Mario",
            last_name="Rossi",
            email="mario@rossibello.com",
            address="Roma",
            cap="20100",
            phone_number="1234567890"
        )


        self.assertEqual(len(gv.client_list), 1)
        self.assertEqual(gv.client_list[0].email, "mario@rossibello.com")
        self.assertEqual(gv.client_list[0].city, "Roma")
        mock_warning.assert_not_called()
        mock_write.assert_called_once()


    @patch("Src.Controllers.ClientController.messagebox.showwarning")
    def test_edit_client_info_failed(self, mock_warning):
        gv.client_list = []
        gv.client_list.append(Client("Milano",  # id
                                     "mario@rossi.com",  # Email
                                     "Mario",  # FirstName
                                     "Rossi",  # LastName
                                     "1",  # id
                                     "1234567890",  #Phone
                                     "20100"  # CAP
                                     ))

        gv.CurrentClient = Client("Napoli",  # City
                                     "f@rb.com",  # Email
                                     "Franchetto",  # FirstName
                                     "Luterr",  #LastName
                                     "2",  # id
                                     "1234567890",  # Phone
                                     "20100"  # CAP
                                     )

        self.cc.edit_client_infos(
            name="Mario",
            last_name="Rossi",
            email="mario@rossibello.com",
            address="Roma",
            cap="20100",
            phone_number="1234567890"
        )

        self.assertEqual(len(gv.client_list), 1)

        mock_warning.assert_called_once()



    @patch("Src.Controllers.ClientController.messagebox.showwarning")
    def test_search_client_success(self, mock_warning):
        gv.client_list = []
        gv.client_list.append(Client("Milano",  # id
                                     "mario@rossi.com",  # Email
                                     "Mario",  # FirstName
                                     "Rossi",  # LastName
                                     "1",  # id
                                     "1234567890",  # Phone
                                     "20100"  # CAP
                                     ))

        result = self.cc.search_client("Mario", "", "", "")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].FirstName, "Mario")
        mock_warning.assert_not_called()
        if len(result) > 0:
            self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()