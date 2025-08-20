from tkinter.messagebox import askyesno
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox
from datetime import datetime
from Src.Class.Appointment import Appointment
from Src.Controllers.APIController import APIController


class AppointmentController:
    def __init__(self):
        print("controller")


    def create_appointment(self, description):

        if gv.CurrentDate is None or gv.CurrentHour is None:
            messagebox.showwarning("Errore", "Seleziona Giorno e Ora!")
            return

        elif datetime.combine(gv.CurrentDate, gv.CurrentHour) < datetime.now():
            messagebox.showwarning("Errore", "Non è possibile selezionare una data passata!")
            return

        else:
           dt = datetime.combine(gv.CurrentDate, gv.CurrentHour)
           appointment = Appointment(description, dt, gv.CurrentUser)
           is_duplicate = any(#appointment.description == description and
                              appointment.date_time == dt and
                              appointment.user == gv.CurrentUser
                              for appointment in gv.appointment_list)
           if is_duplicate:
               messagebox.showwarning("Errore", "Esiste già un appuntamento in questa data e ora!")
               return

           gv.appointment_list.append(appointment)
           APIController.write_appointment_on_csv()

    def find_appointment(self):
        if gv.CurrentDate is None or gv.CurrentHour is None:
            messagebox.showwarning("Errore", "Seleziona Giorno e Ora!")
            return None
        for app in gv.appointment_list:
            if app.date_time == datetime.combine(gv.CurrentDate, gv.CurrentHour) and app.user.user_id == gv.CurrentUser.user_id:
                return gv.appointment_list.index(app)

        return None

    def update_appointment(self,index ,new_time, new_description):

        gv.appointment_list[index].date_time = datetime.combine(gv.CurrentDate, new_time)
        gv.appointment_list[index].description = new_description
        APIController.write_appointment_on_csv()

    def delete_appointment(self):

        answer = askyesno("Cancellazione", "Sei sicuro di voler cancellare l'appuntamento?")
        if answer:
            index = self.find_appointment()
            gv.appointment_list.pop(index)
            if gv.appointment_list:
                APIController.write_appointment_on_csv()
                messagebox.showinfo("Successo", "Appuntamento eliminato con successo")
            else:
                import pandas as pd
                df = pd.DataFrame(columns=["DateTime", "User ID", "Description"])
                df.to_csv(gv.Appointment_file_path, index=False)
                messagebox.showinfo("Successo", "Ultimo appuntamento eliminato, lista ora vuota")


