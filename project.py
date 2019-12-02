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

height = tk.StringVar()
width = tk.StringVar()
depth = tk.StringVar()
diameter = tk.StringVar()


global frame
frame = tk.Frame(main_window)


def create_main_window():
    title = tk.Label(main_window, text="Wrapping ordering system", font="default 16 bold")
    title.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    selection.set(CONTAINERS[0])
    selection_label = tk.Label(main_window, text="Please select which container the wrapping is for:", padx=10)
    selection_label.grid(column=0, row=1, columnspan=3, sticky=tk.W)
    container_option_menu = tk.OptionMenu(main_window, selection, *CONTAINERS, command=create_form)
    container_option_menu.grid(column=0, row=2, padx=10, sticky=tk.W)

    create_form()

    quit_button = tk.Button(main_window, text="Quit", font=button_font, command=main_window.quit, padx=5, pady=5)
    quit_button.grid(column=1, row=20, padx=10, pady=10)


def create_form(*args):
    global frame #use globally defined frame
    try:
        frame.destroy() # if frame already exists, destroy it
    finally:
        pass
    #reset all variables to default values
    height.set('0')
    width.set('0')
    depth.set('0')
    diameter.set('0')

    #reinitialise frame
    frame = tk.Frame(main_window)
    frame.grid(column=0, row=3)
    selected_type = selection.get() # get the selected type for decision
    if selected_type == "Cube":
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0)
        height_entry = tk.Entry(frame, textvariable=height)
        height_entry.grid(column=0, row=1)
    elif selected_type == "Cuboid":
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0)
        height_entry = tk.Entry(frame, textvariable=height)
        height_entry.grid(column=0, row=1)
        width_label = tk.Label(frame, text="Width:")
        width_label.grid(column=0, row=2)
        width_entry = tk.Entry(frame,textvariable=width)
        width_entry.grid(column=0, row=3)
        depth_label = tk.Label(frame, text="Depth:")
        depth_label.grid(column=0, row=4)
        depth_entry = tk.Entry(frame, textvariable=depth)
        depth_entry.grid(column=0, row=5)
    elif selected_type == 'Cylinder':
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0)
        height_entry = tk.Entry(frame, textvariable=height)
        height_entry.grid(column=0, row=1)
        diameter_label = tk.Label(frame, text="Diameter:")
        diameter_label.grid(column=0, row=2)
        diameter_entry = tk.Entry(frame, textvariable=diameter)
        diameter_entry.grid(column=0, row=3)
    

create_main_window()
main_window.mainloop()
