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
        else:
           dt = datetime.combine(gv.CurrentDate, gv.CurrentHour)
           appointment = Appointment(description, dt, gv.CurrentUser)
           is_duplicate = any(appointment.description == description and
                              appointment.date_time == dt and
                              appointment.user == gv.CurrentUser
                              for appointment in gv.appointment_list)
           if is_duplicate:
               messagebox.showwarning("Errore", "Esiste già un appuntamento in questa data e ora!")
               return

           gv.appointment_list.append(appointment)
           APIController.write_appointment_on_csv()


