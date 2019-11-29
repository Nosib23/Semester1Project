import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title("Checkout System")
main_window.geometry("1000x600")

button_font = "default 16"
CONTAINERS = ['Cube', 'Cuboid', 'Cylinder']
COLOURS = ['purple', 'DarkSlateGray4', 'deep sky blue', 'light sea green', 'VioletRed2', 'gold']

selection = tk.StringVar()
selected_color = tk.StringVar()
selected_color.set(COLOURS[0])


def create_main_window():
    title = tk.Label(main_window, text="Wrapping ordering system", font="default 16 bold")
    title.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    height_label = tk.Label(main_window, text="Height:")
    height_entry = tk.Entry(main_window)
    width_label = tk.Label(main_window, text="Width:")
    width_entry = tk.Entry(main_window)
    depth_label = tk.Label(main_window, text="Depth:")
    depth_entry = tk.Entry(main_window)
    diameter_label = tk.Label(main_window, text="Diameter:")
    diameter_entry = tk.Entry(main_window)


    selection.set('Select')
    selection_label = tk.Label(main_window, text="Please select which container the wrapping is for:", padx=10)
    selection_label.grid(column=0, row=1, columnspan=3, sticky=tk.W)
    container_option_menu = tk.OptionMenu(main_window, selection, *CONTAINERS, command=create_form)
    container_option_menu.grid(column=0, row=2, padx=10, sticky=tk.W)

    quit_button = tk.Button(main_window, text="Quit", font=button_font, command=main_window.quit, padx=5, pady=5)
    quit_button.grid(column=1, row=20, padx=10, pady=10)


def create_form(*args):
    selected_type = selection.get()
    if selected_type == "Cube":
        pass
    elif selected_type == "Cuboid":
        pass   
    else:
        pass
    

# var.trace watches variable for changes and triggers function

create_main_window()
main_window.mainloop()
