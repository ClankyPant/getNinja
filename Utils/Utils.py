import tkinter as tk


class Utils:

    @staticmethod
    def createDefaultFrame(master, padX, padY):
        container = tk.Frame(master)
        container["padx"] = padX
        container["pady"] = padY
        container.pack()
        return container
