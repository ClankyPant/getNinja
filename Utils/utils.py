import tkinter as tk


class Utils:

    @staticmethod
    def createDefaultFrame(master, padx, pady):
        container = tk.Frame(master)
        container["padx"] = padx
        container["pady"] = pady
        container.pack()
        return container

    @staticmethod
    def showMsg(title, value):
        tk.messagebox.showinfo(title, value)