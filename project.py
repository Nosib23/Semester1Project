import tkinter as tk
from tkinter import messagebox
from math import pi

main_window = tk.Tk()
main_window.title("Checkout System")

CONTAINERS = ['Cube', 'Cuboid', 'Cylinder']
COLOURS = ['purple', 'DarkSlateGray4', 'deep sky blue', 'light sea green', 'VioletRed2', 'gold']
CHEAP = 0.4
EXPENSIVE = 0.75
BOW = 1.5
CARD = 0.5
CARD_LETTER = 0.02

button_font = "default 12"
selection = tk.StringVar()
selected_color = tk.StringVar()
selected_color.set(COLOURS[0])
paper_type = tk.StringVar()
paper_type.set('Cheap')
bow = tk.IntVar()
gift_tag = tk.IntVar()
gift_tag_text = tk.StringVar()
basket = {}
no_of_items = tk.StringVar()
no_of_items.set('0')
total_cost_str = tk.StringVar()
total_cost_str.set('£0.00')
total_cost = 0.0

height_sv = tk.StringVar()
width_sv = tk.StringVar()
length_sv = tk.StringVar()
diameter_sv = tk.StringVar()

canvas_wh = 300
canvas = tk.Canvas(main_window, width=canvas_wh, height=canvas_wh)
frame = tk.Frame(main_window)


def create_main_window():
    title = tk.Label(main_window, text="Wrapping ordering system", font="default 16 bold")
    title.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    #column 1 & 2
    selection.set(CONTAINERS[0])
    selection_label = tk.Label(main_window, text="Please select which container the wrapping is for:", padx=10)
    selection_label.grid(column=0, row=1, columnspan=3)

    container_label = tk.Label(main_window, text="Container type:", padx=10)
    container_label.grid(column=0, row=2)
    container_om = tk.OptionMenu(main_window, selection, *CONTAINERS, command=create_form)
    container_om.grid(column=1, row=2, padx=10)

    paper_label = tk.Label(main_window, text="Paper type:")
    paper_label.grid(column=0, row=3)
    paper_om = tk.OptionMenu(main_window, paper_type, 'Cheap', 'Expensive', command=create_canvas)
    paper_om.grid(column=1, row=3)

    colour_label = tk.Label(main_window, text="Colour choice:")
    colour_label.grid(column=0, row=4)
    colour_om = tk.OptionMenu(main_window, selected_color, *COLOURS, command=create_canvas)
    colour_om.grid(column=1, row=4, padx=10)

    create_form()
    
    #column 3
    canvas_label = tk.Label(main_window, text="Paper preview:")
    canvas_label.grid(column=3, row=1)
    canvas.grid(column=3, row=2, rowspan=10, padx=10)
    
    create_canvas()

    #column 4
    add_button = tk.Button(main_window, text="Add to Basket", command=add_to_basket, font=button_font, padx=5, pady=5)
    add_button.grid(column=4, row=2, padx=20, pady=5)
    view_basket_button = tk.Button(main_window, text="View Basket", command=view_basket, font=button_font, padx=5, pady=5)
    view_basket_button.grid(column=4, row=3, padx=20, pady=5)
    print_button = tk.Button(main_window, text="Print Quote", command=print_quote, font=button_font, padx=5, pady=5)
    print_button.grid(column=4, row=4, padx=20, pady=5)

    #column 5 & 6
    basket_label = tk.Label(main_window, text="Basket:")
    basket_label.grid(column=5, row=1, sticky=tk.W)

    no_label = tk.Label(main_window, text="Number of items:")
    no_label.grid(column=5, row=2, sticky=tk.W)
    items_label = tk.Label(main_window, textvariable=no_of_items)
    items_label.grid(column=6, row=2, sticky=tk.W)
    total_cost_lbl = tk.Label(main_window, text="Total cost:")
    total_cost_lbl.grid(column=5, row=3, sticky=tk.W)
    total_cost_label = tk.Label(main_window, textvariable=total_cost_str)
    total_cost_label.grid(column=6, row=3, sticky=tk.W)

    quit_button = tk.Button(main_window, text="Quit", font=button_font, command=main_window.quit, padx=5, pady=5)
    quit_button.grid(column=6, row=20, padx=10, pady=10)


def add_to_basket():
    noi = int(no_of_items.get())
    height = int(height_sv.get())   
    height_sv.set('0')
    width = int(width_sv.get())
    width_sv.set('0')
    length = int(length_sv.get())
    length_sv.set('0')
    diameter = int(diameter_sv.get())
    diameter_sv.set('0')
    bow_added = 'no'
    tag_added = 'no'
    tag_text = ''

    selected = selection.get()
    if selected == CONTAINERS[0]: # cube
        wrapper_size = (height * 4 + 6) * (height * 3 + 6)
    elif selected == CONTAINERS[1]: # cuboid
        wrapper_size = ((height * 2) + width + 6) * ((length*2) + (height*2) + 6)
    elif selected == CONTAINERS[2]: # cylinder
        circumference = pi * diameter
        wrapper_size = (circumference + 6) * (height + (diameter*2) + 6)
    
    pt = paper_type.get()
    if pt == 'Cheap':
        price = wrapper_size * CHEAP
    elif pt == 'Expensive':
        price = wrapper_size * EXPENSIVE

    price = price / 100

    if bow.get():
        price += BOW
        bow_added = 'yes'
        bow.set(0)

    if gift_tag.get():
        tag_text = gift_tag_text.get()
        price += CARD
        price += len(tag_text) * CARD_LETTER
        tag_added = 'yes'
        gift_tag.set(0)
        gift_tag_text.set('')

    global total_cost
    total_cost += price
    total_cost_str.set(f'£{total_cost:.2f}')

    noi += 1
    no_of_items.set(f'{noi}')
    basket.setdefault(f'Item {noi}', [f'Price: {price:.2f} pounds', f'Type: {selected}', f'Bow: {bow_added}', f'Gift Card: {tag_added}', f'Card text: {tag_text}'])


def create_form(*args):
    '''initialises and switches form on user selection of container type'''
    
    global frame #use globally defined frame
    try:
        frame.destroy() # if frame already exists, destroy it to reset old form
    finally:
        pass
    #reset all variables to default values
    height_sv.set('0')
    width_sv.set('0')
    length_sv.set('0')
    diameter_sv.set('0')

    #reinitialise frame
    frame = tk.Frame(main_window)
    frame.grid(column=0, row=5, columnspan=2)
    selected_type = selection.get() # get the selected type for decision
    
    if selected_type == "Cube":
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0, padx=10)
        height_entry = tk.Entry(frame, textvariable=height_sv)
        height_entry.grid(column=1, row=0, padx=10, pady=10)
    elif selected_type == "Cuboid":
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0, padx=10)
        height_entry = tk.Entry(frame, textvariable=height_sv)
        height_entry.grid(column=1, row=0, padx=10, pady=10)
        width_label = tk.Label(frame, text="Width:")
        width_label.grid(column=0, row=1, padx=10)
        width_entry = tk.Entry(frame,textvariable=width_sv)
        width_entry.grid(column=1, row=1, padx=10, pady=10)
        length_label = tk.Label(frame, text="Length:")
        length_label.grid(column=0, row=2, padx=10)
        length_entry = tk.Entry(frame, textvariable=length_sv)
        length_entry.grid(column=1, row=2, padx=10, pady=10)
    elif selected_type == 'Cylinder':
        height_label = tk.Label(frame, text="Height:")
        height_label.grid(column=0, row=0, padx=10)
        height_entry = tk.Entry(frame, textvariable=height_sv)
        height_entry.grid(column=1, row=0, padx=10, pady=10)
        diameter_label = tk.Label(frame, text="Diameter:")
        diameter_label.grid(column=0, row=1, padx=10)
        diameter_entry = tk.Entry(frame, textvariable=diameter_sv)
        diameter_entry.grid(column=1, row=1, padx=10, pady=10)

    bow_label = tk.Label(frame, text="Bow needed:")
    bow_label.grid(column=0, row=3)
    bow_check = tk.Checkbutton(frame, variable=bow)
    bow_check.grid(column=1, row=3)
    
    tag_label = tk.Label(frame, text="Gift tag needed:")
    tag_label.grid(column=0, row=4)
    tag_check = tk.Checkbutton(frame, variable=gift_tag)
    tag_check.grid(column=1, row=4)
    tag_needed_label = tk.Label(frame, text="Gift tag text")
    tag_needed_label.grid(column=0, row=5)
    tag_entry = tk.Entry(frame, textvariable=gift_tag_text)
    tag_entry.grid(column=1, row=5)


def create_canvas(*args):
    '''creates canvas for paper preview on user selection of paper type or colour'''
    
    canvas.delete('all')
    paper_selection = paper_type.get()

    if paper_selection == 'Cheap':
        draw_hexagon()
    elif paper_selection == 'Expensive':
        draw_triangles()
    

def draw_hexagon():
    '''draws hexagon "cheap" wrapping paper in the canvas'''

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


def draw_triangles():
    ''' draws triangle paper in the canvas '''
    
    
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


def print_quote():
    with open("quote.txt", "w+") as f:
        f.write('Quote: \n \n')
        for k, v in basket.items():
            f.write(k +  '\n')
            for value in v:
                f.write(value + '\n')
        f.write(f'Total cost: {total_cost:.2f} pounds.' + '\n')
        messagebox.showinfo('Saved to file', 'Quote was saved to file "quote.txt" in main directory.')


def view_basket():
    basket_contents = tk.StringVar()
    add_window = tk.Toplevel(main_window)
    add_window.title("Basket")

    title = tk.Label(add_window, text="Basket", font="default 16 bold")
    title.grid(column=0, row=0)
    
    content = tk.Label(add_window, textvariable=basket_contents)
    content.grid(column=0, row=1)

    for k, v in basket.items():
        contents = basket_contents.get()
        contents = contents + '\n' + f'''{k}:
{v[0]}
{v[1]}
{v[2]}
---'''
        basket_contents.set(contents)


create_main_window()
main_window.mainloop()
