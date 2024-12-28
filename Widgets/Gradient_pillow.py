from PIL import Image,ImageTk,ImageDraw
import tkinter as tk

def creategradient(width,height):
    gradient = Image.new("RGBA",[width,height])
    draw = ImageDraw.Draw(gradient)

    color1 = (116, 235, 213,100)
    color2 = (172, 182, 229,100)

    for y in range(height):
        alpha = int(255 * y / height)
        color = tuple(
            int(color1[i] * (1 - y / height) + color2[i] * (y / height))
            for i in range(3)
        ) + (alpha,)
        draw.line([(0, y), (width, y)], fill=color)

    return gradient

gradient_image = creategradient(400,200)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Convert the PIL Image to a PhotoImage object
gradient_photo = ImageTk.PhotoImage(gradient_image)

# Create a reference to keep the image from being garbage collected
canvas.gradient_photo = gradient_photo

# Display the gradient image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=gradient_photo)

root.mainloop()