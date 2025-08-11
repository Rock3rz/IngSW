import os


# Stato applicativo
isAdminUser = False
canEnter = False

CurrentUser = None

# Indirizzi database (relativi alla root del progetto)
User_file_path = "DB/user.csv"
Clients_file_path = "DB/clients.csv"
Brand_file_path = "DB/brand.csv"
Model_file_path = "DB/model.csv"

# Collezioni condivise in memoria
user_list = []
client_list = []
brand_list = []
model_list = []
vehicle_list = []

# Entità correnti selezionate nella GUI
CurrentClient = None
CurrentBrand = None
CurrentModel = None


# Controller centralizzati (inizializzati pigramente)
account_controller = None
client_controller = None
vehicle_controller = None
api_controller = None


def init_controllers():

    #Inizializza e centralizza le istanze dei controller.


    global account_controller, client_controller, vehicle_controller, api_controller

    if all([account_controller, client_controller, vehicle_controller, api_controller]):
        return

    # Creazione directory DB se mancante
    os.makedirs(os.path.dirname(User_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(Clients_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(Brand_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(Model_file_path), exist_ok=True)

    # Import locali per evitare cicli
    from Src.Controllers.AccountController import AccountController
    from Src.Controllers.ClientController import ClientController
    from Src.Controllers.VehicleController import VehicleController
    from Src.Controllers.APIController import APIController

    # Istanza API una volta per popolamento liste da CSV
    api_controller = APIController()

    # Altri controller applicativi condivisi
    account_controller = AccountController()
    client_controller = ClientController()
    vehicle_controller = VehicleController()

