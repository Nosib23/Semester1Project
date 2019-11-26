import tkinter as tk

main = tk.Tk()

canvas_wh = 300
selected_fill = "blue"

choice = tk.IntVar()

trangle_radio = tk.Radiobutton(main, text="Triangle", variable=choice, value=1).pack()
honeycomb_radio = tk.Radiobutton(main, text="Honeycomb", variable=choice, value=2).pack()

canvas = tk.Canvas(main, width=canvas_wh, height=canvas_wh)
canvas.pack()

start = 0
end = 50

# declare using loop and offset each point from the starting position


def create_hexagon():
    default_x_point = [0, 15, 45, 60, 45, 15]
    x_point = default_x_point
    y_point = [30, 0, 0, 30, 60, 60]
    offset = 60
    fill = selected_fill
    for row in range(5):
        if row % 2 == 0:
            even_row = False
            columns = 5
        else:
            even_row = True
            columns = 6
        
        for column in range(columns):
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
    fill = selected_fill
    point1 = (0, canvas_wh)
    point2 = ((canvas_wh / 2), 0)
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
            (point2[0], (point2[1] + 60))
        )
        point3 = (
            ((point3[0] - 30), point3[1])
        )

        if fill == selected_fill:
            fill = "white"
        else:
            fill = selected_fill


def draw(*args):
    value = choice.get()
    if value == 1:
        canvas.delete('all')
        create_triangles()
    elif value == 2:
        canvas.delete('all')
        create_hexagon()

choice.trace('r', draw)

create_hexagon()
# create_triangles()
main.mainloop()
