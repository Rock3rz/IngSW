import tkinter as tk
from Gui.GUI import Gui
import Src.GlobalVariables.GlobalVariables as gv



#funzione main che conterrà il main loop
if __name__ == '__main__':
    root = tk.Tk()
    root.title('AutoneThor')


    #per tutto il resto
    root.geometry('1920x1080')

    # Inizializza e centralizza i controller (carica le liste da CSV)
    gv.init_controllers()

    app = Gui(root)

    root.mainloop()

