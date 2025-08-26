from datetime import datetime
from Src.Class.Quote import Quote
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox
from Src.Controllers.APIController import APIController


class QuoteController:

    def create_quote(self,quote_id_str, client_id_str, vehicle_id_str, start_date, end_date, price):
        if not all([quote_id_str, client_id_str, vehicle_id_str, start_date, end_date, price]):
            messagebox.showwarning(
                "Campi vuoti",
                "Seleziona tutte le informazioni affinché vengano inserite!")
            return


        client_id = int(client_id_str.split()[0])
        quote_id = int(quote_id_str.split()[0])
        vehicle_id = int(vehicle_id_str.split()[0])

        tmp_vehicle = gv.vehicle_recovery(vehicle_id)

        if not tmp_vehicle.is_available:
            messagebox.showwarning(
                "Preventivo non possibile",
                "Il veicolo risulta già associato ad un altro preventivo")
            return
        else:
            tmp_vehicle.is_available = False



        if gv.quote_list:
            is_duplicate = any(int(q.Client.ID) == int(client_id) and
                               int(q.Vehicle.vehicle_id) == int(vehicle_id) and
                               float(q.Price) == float(price)
                               for q in gv.quote_list)
            if is_duplicate:
                messagebox.showwarning(
                    "Preventivo già esistente",
                    "Il cliente selezionato ha già un preventivo attivo per questo veicolo!")
                return


        new_quote = Quote(gv.client_recovery(client_id),
                  False,
                  datetime.strptime(end_date, "%d/%m/%Y").date(),
                  quote_id,
                  datetime.strptime(start_date, "%d/%m/%Y").date(),
                  gv.CurrentUser,
                  gv.vehicle_recovery(vehicle_id),
                  price)

        gv.quote_list.append(new_quote)

        APIController.write_quote_on_csv()

        APIController.write_vehicle_on_csv()


        for quote in gv.quote_list:
            print(f"Client: {quote.Client.FirstName}")
            print(f"Confirmed: {quote.Confirmed}")
            print(f"EndDate: {quote.EndDate}")
            print(f"ID: {quote.id}")
            print(f"StartDate: {quote.StartDate}")
            print(f"User: {quote.User.firstName}")
            print(f"Vehicle: {quote.Vehicle.model.name}")
            print(f"Price: {quote.Price}")
            print("-" * 30)

    def delete_quote(self):
        askyesno = messagebox.askyesno("Conferma", "Vuoi eliminare il preventivo selezionato?")
        if askyesno:
            if gv.CurrentQuote in gv.quote_list:
                gv.CurrentQuote.Vehicle.is_available = True
                gv.CurrentQuote.Vehicle.sold = False
                gv.quote_list.remove(gv.CurrentQuote)

                if gv.quote_list:

                    APIController.write_quote_on_csv()
                    messagebox.showinfo("Successo", "Preventivo eliminato con successo")
                else:
                    import pandas as pd
                    df = pd.DataFrame(columns=["Client", "Confirmed", "EndDate", "ID", "StartDate", "User", "Vehicle", "Price"])
                    df.to_csv(gv.Quote_file_path, index=False)
                    messagebox.showinfo("Successo", "Ultimo preventivo eliminato, lista ora vuota")

    def confirm_quote(self):
        response = messagebox.askyesno("Conferma", "Vuoi confermare il preventivo selezionato?")
        if response:
            if gv.CurrentQuote:
                gv.CurrentQuote.Confirmed = True
                gv.CurrentQuote.Vehicle.sold = True
                gv.CurrentQuote.Vehicle.is_available = False
                APIController.write_vehicle_on_csv()
                APIController.write_quote_on_csv()
                messagebox.showinfo("Successo", "Preventivo confermato con successo")
        else:
            return

