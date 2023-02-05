import tkinter as tk
from PIL import Image, ImageTk
import time

def add_100():
    global result
    result += 100
    result_label.config(text=str(result))

def close_window():
    root.destroy()

def animate_ball():
    global angle, image_tk
    angle = (angle + 10) % 360
    image = Image.open("ball.png")
    image = image.rotate(angle)
    image_tk = ImageTk.PhotoImage(image)
    ball_label.config(image=image_tk)
    root.after(100, animate_ball)

root = tk.Tk()
root.title("Janela com Botões e Bola Girando")

result = 0
result_label = tk.Label(root, text=str(result), font=("Helvetica", 24))
result_label.pack()

start_button = tk.Button(root, text="Começar", bg="red", command=add_100, font=("Helvetica", 24))
start_button.pack(fill="x")

end_button = tk.Button(root, text="Finalizar", bg="red", command=close_window, font=("Helvetica", 24))
end_button.pack(fill="x")

angle = 0
image = Image.open("ball.jpg")
image_tk = ImageTk.PhotoImage(image)
ball_label = tk.Label(root, image=image_tk)
ball_label.pack()

animate_ball()
root.mainloop()
