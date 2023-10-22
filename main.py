import tkinter as tk
from main_menu import main_menu


def start_window():
    main_window = tk.Tk()
    main_window.geometry("1400x700")
    main_window.title("To-do list")
    main_window.resizable(False, False)
    main_menu(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    start_window()
