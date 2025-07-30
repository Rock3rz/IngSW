import tkinter as tk
from Gui.GUI import Gui


#funzione main che conterrà il main loop
if __name__ == '__main__':
    root = tk.Tk()
    root.title('AppDelleMacchine')
    root.geometry('1920x1080')

    app = Gui(root)
    root.mainloop()


