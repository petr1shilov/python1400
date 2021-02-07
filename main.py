import tkinter as tk 

def move_by_key(event):
    if event.keysym == 'Up':
        canvas.move(oval , 0, -20)
    if event.keysym == 'Down':
        canvas.move(oval , 0, 20)
    if event.keysym == 'Right':
        canvas.move(oval , 20, 0)
    if event.keysym == 'Left':
        canvas.move(oval , -20, 0)
    if event.keysym == 'Escape':
        exit()

window = tk.Tk() #создание нового окна 

# label = tk.Label(
#     text='Hello', 
#     fg='purple', 
#     bg='#EEA132', 
#     width=20, 
#     height=20
# )
# label.pack() #Обновление экрана 

# button = tk.Button(
#     text='нажми меня',
#     width=25,
#     height=5,
#     fg='red',
#     bg='white'
# )
# button.pack()

# canvas = tk.Canvas(
#     window, 
#     bg='#0ff',
#     width= 700,
#     height=700
# )


# canvas.create_line(
#     (0, 0), (100, 100), (100, 200), (0, 0),
#      dash=(4, 2),
#      fill='purple',
#       width=5 
# )



# oval = canvas.create_oval(
#     (200, 200), (300, 300),
#     outline='green',
#     fill='red',
#     width=5
# )


# points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
 
# canvas.create_polygon(
#     points, outline='red', 
#     fill='green', width=2
# )


# canvas.create_rectangle(
#     (230, 10), (290, 60)
# )

size = 400
amount = 8 
canvas1 = tk.Canvas(
    window,
    bg='yellow',
    width= size,
    height=size
)

for x in range(0, size, size // amount):
    canvas1.create_line((x, 0), (x, size), fill='purple')
    canvas1.create_line((0, x), (size, x), fill='purple')

canvas1.pack()
# window.bind("<KeyPress>", move_by_key)



window.mainloop() # запуск клавного цикла