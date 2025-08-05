import tkinter as tk
from Gui.GUI import Gui
import os
from Controllers.APIController import APIController



#funzione main che conterrà il main loop
if __name__ == '__main__':
    root = tk.Tk()
    root.title('AppDelleMacchine')
    root.geometry('1920x1080')
    Api = APIController()
    app = Gui(root)

    root.mainloop()
