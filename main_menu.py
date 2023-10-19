import tkinter as tk
from tkinter import *


def sluiten(main_window):
    main_window.destroy()


def main_menu(main_window):
    for widget in main_window.winfo_children():
        widget.destroy()

    show_create_to = Button(main_window, text="Kiez karakter", width=30, height=2, borderwidth=4)
    show_create_to.place(x=600, y=100)

    show_all = Button(main_window, text="Karakter aanmaken", width=30, height=2, borderwidth=4)
    show_all.place(x=600, y=200)

    show_all = Button(main_window, text="Instellingen", width=30, height=2, borderwidth=4)
    show_all.place(x=600, y=300)

    sluit_knop = Button(main_window, text="Sluiten", width=30, height=2, borderwidth=4, command=lambda: sluiten(main_window))
    sluit_knop.place(x=600, y=400)
