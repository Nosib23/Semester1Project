import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title("Checkout System")

button_font = "default 16"

def create_main_menu():
    title = tk.Label(main_window, text="Checkout", font="default 20 bold")
    title.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    

    quit_button = tk.Button(main_window, text="Quit", font=button_font, command=main_window.quit, padx=10, pady=10)
    quit_button.grid(column=1, row=6, padx=10, pady=10)


create_main_menu()
main_window.mainloop()