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
paper_type = tk.StringVar()

height = tk.StringVar()
width = tk.StringVar()
depth = tk.StringVar()
diameter = tk.StringVar()

canvas_wh = 300
global canvas
canvas = tk.Canvas(main_window, width=canvas_wh, height=canvas_wh)

global frame
frame = tk.Frame(main_window)


def create_main_window():
    title = tk.Label(main_window, text="Wrapping ordering system", font="default 16 bold")
    title.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    selection.set(CONTAINERS[0])
    selection_label = tk.Label(main_window, text="Please select which container the wrapping is for:", padx=10)
    selection_label.grid(column=0, row=1, columnspan=3, sticky=tk.W)

    container_label = tk.Label(main_window, text="Container type:", padx=10)
    container_label.grid(column=0, row=2)
    container_om = tk.OptionMenu(main_window, selection, *CONTAINERS, command=create_form)
    container_om.grid(column=1, row=2, padx=10, sticky=tk.W)
    
    canvas.grid(column=3, row=2, rowspan=10)

    paper_label = tk.Label(main_window, text="Paper type:")
    paper_label.grid(column=0, row=3)
    paper_om = tk.OptionMenu(main_window, paper_type, 'Cheap', 'Expensive', command=create_canvas)
    paper_om.grid(column=1, row=3)

    colour_label = tk.Label(main_window, text="Colour choice:")
    colour_label.grid(column=0, row=4)
    colour_om = tk.OptionMenu(main_window, selected_color, *COLOURS, command=create_canvas)
    colour_om.grid(column=1, row=4, padx=10, sticky=tk.W)

    create_form()

    quit_button = tk.Button(main_window, text="Quit", font=button_font, command=main_window.quit, padx=5, pady=5)
    quit_button.grid(column=1, row=20, padx=10, pady=10)


def create_form(*args):
    '''initialises and switches form on user selection of container type'''
    
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
    frame.grid(column=0, row=5)
    selected_type = selection.get() # get the selected type for decision
    if selected_type == "Cube":
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0, padx=10)
        height_entry = tk.Entry(frame, textvariable=height)
        height_entry.grid(column=0, row=1, padx=10)
    elif selected_type == "Cuboid":
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0, padx=10)
        height_entry = tk.Entry(frame, textvariable=height)
        height_entry.grid(column=0, row=1, padx=10)
        width_label = tk.Label(frame, text="Width:")
        width_label.grid(column=0, row=2, padx=10)
        width_entry = tk.Entry(frame,textvariable=width)
        width_entry.grid(column=0, row=3, padx=10)
        depth_label = tk.Label(frame, text="Depth:")
        depth_label.grid(column=0, row=4, padx=10)
        depth_entry = tk.Entry(frame, textvariable=depth)
        depth_entry.grid(column=0, row=5, padx=10)
    elif selected_type == 'Cylinder':
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0, padx=10)
        height_entry = tk.Entry(frame, textvariable=height)
        height_entry.grid(column=0, row=1, padx=10)
        diameter_label = tk.Label(frame, text="Diameter:")
        diameter_label.grid(column=0, row=2, padx=10)
        diameter_entry = tk.Entry(frame, textvariable=diameter)
        diameter_entry.grid(column=0, row=3, padx=10)
    

def create_canvas(*args):
    '''creates canvas for paper preview on user selection of paper type or colour'''
    
    canvas.delete('all')
    paper_selection = paper_type.get()

    if paper_selection == 'Cheap':
        create_triangles()
    elif paper_selection == 'Expensive':
        create_hexagon()
    

def create_hexagon():
    default_x_point = [0, 15, 45, 60, 45, 15]
    x_point = default_x_point
    y_point = [30, 0, 0, 30, 60, 60]
    offset = 60
    fill = selected_color.get()
    for row in range(5):
        if row % 2 == 0:
            even_row = False
            columns = 5
        else:
            even_row = True
            columns = 6
        
        for x in range(columns):
            canvas.create_polygon(
                x_point[0], y_point[0],
                x_point[1], y_point[1],
                x_point[2], y_point[2],
                x_point[3], y_point[3],
                x_point[4], y_point[4],
                x_point[5], y_point[5],
                fill=fill, outline="black"
            )
            x_point = [x + offset for x in x_point]
        
        if not even_row:
            x_point = [x - 45 for x in default_x_point]
        else: 
            x_point = default_x_point
        
        y_point = [y + offset for y in y_point]


def create_triangles():
    fill = selected_color.get()
    point1 = (0, canvas_wh)
    point2 = (canvas_wh / 2, 0)
    point3 = (canvas_wh, canvas_wh)

    for x in range(5):
        canvas.create_polygon(
            point1[0], point1[1],
            point2[0], point2[1],
            point3[0], point3[1],
            fill=fill, outline="black"
        )

        point1 = (
            (point1[0] + 30, point1[1])
        )
        point2 = (
            (point2[0], point2[1] + 60)
        )
        point3 = (
            (point3[0] - 30, point3[1])
        )

        if fill == selected_color.get():
            fill = "white"
        else:
            fill = selected_color.get()


create_main_window()
main_window.mainloop()
