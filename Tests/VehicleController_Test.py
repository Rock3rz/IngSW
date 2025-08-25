import unittest
from unittest.mock import patch
from Src.Controllers.VehicleController import VehicleController
from Src.Class.Vehicle import Vehicle, FuelType, Model

import Src.GlobalVariables.GlobalVariables as gv

class TestVehicleController(unittest.TestCase):
    def setUp(self):
        self.vc = VehicleController()
        gv.vehicle_list = []
        self.genericModel = Model("Fiat", "Panda", "1000", "80", "1")
        gv.model_list.append(self.genericModel)
        self.genericAuto = Vehicle(
            model = gv.model_list[0],
            registration_year= 2000,
            color = "Blue",
            fuel_type = FuelType.GPL,
            vehicle_id = "1",
            is_available = True,
            km = "100",
            number_plate = "ABC123",
            price = "1000"


        )


    @patch("Src.Controllers.VehicleController.APIController.write_vehicle_on_csv")
    @patch("Src.Controllers.VehicleController.messagebox.showwarning")
    def test_create_vehicle_success(self, mock_warning, mock_write):
        self.vc.create_vehicle(
            vehicle_id = "1",
            model_id = "1",
            year = "2020",
            color = "blue",
            fuel_type = FuelType.GPL,
            is_available = True,
            km = "100",
            plate = "ABC123",
            price = "1000",

        )


        self.assertEqual(len(gv.vehicle_list), 1)
        mock_warning.assert_not_called()
        mock_write.assert_called_once()
        if len(gv.vehicle_list) > 0:
            self.assertEqual(gv.vehicle_list[0].vehicle_id, "1")
            self.assertEqual(gv.vehicle_list[0].model.brand, "Fiat")

    @patch("Src.Controllers.VehicleController.messagebox.showwarning")
    def test_create_vehicle_failed(self, mock_warning):
        self.vc.create_vehicle(
            vehicle_id="1",
            model_id="1",
            year="2020",
            color="blue",
            fuel_type=FuelType.GPL,
            is_available=True,
            km="",
            plate="ABC123",
            price="1000",

        )

        self.assertEqual(len(gv.vehicle_list), 0)
        mock_warning.assert_called_once()



    #@patch("Src.Controllers.VehicleController.APIController.write_vehicle_on_csv")
    @patch("Src.Controllers.VehicleController.messagebox.showwarning")

    def test_not_vehicle_selected(self,mock_warning):
        gv.vehicle_list = []
        gv.CurrentVehicle = None
        self.vc.delete_vehicle()

        mock_warning.assert_called_once()

    @patch("Src.Controllers.VehicleController.messagebox.showwarning")
    def test_delete_vehicle_not_in_list(self, mock_warning):
        gv.vehicle_list = []
        gv.current_vehicle = self.genericAuto
        result = self.vc.delete_vehicle()

        mock_warning.assert_called_once()
        self.assertIsNone(result, "nessun ritorno")

    @patch("Src.Controllers.VehicleController.APIController.write_vehicle_on_csv")
    @patch("Src.Controllers.VehicleController.messagebox.askyesno", return_value=True)
    def test_delete_vehicle_success(self, mock_askyesno, mock_write):
        gv.vehicle_list = []
        gv.vehicle_list.append(self.genericAuto)
        gv.CurrentVehicle = self.genericAuto

        self.assertEqual(len(gv.vehicle_list), 1)

        self.vc.delete_vehicle()
        mock_askyesno.assert_called_once()
        mock_write.assert_called_once()
        self.assertEqual(len(gv.vehicle_list), 0)


if __name__ == "__main__":
    unittest.main()