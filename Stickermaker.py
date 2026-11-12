import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from rembg import remove
import os
#function to create a sticker
def create_sticker():
    #allow the user to upload an image
    file = filedialog.askopenfilename(filetypes=[("Images", "*.png *. jpg *.jpeg")])
    if file:
        #open the uploaded image
        image = Image.open(file)
        #remove the background using AI
        sticker = remove(image)
        #resize the sticker
        sticker.thumbnail((512, 512))
       # Create a Stickers folder in the project
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Stickers")
        os.makedirs(folder, exist_ok=True)
        # Save sticker in the Stickers folder
        name = os.path.splitext(os.path.basename(file))[0]
        path = os.path.join(folder, name + "_sticker.png")
        #show success message
        messagebox.showinfo("Succes", "Sticker created successfully!")
#create the app window
root = tk.Tk()#root is the screen/window
root.title("AI Sticker Maker")
root.geometry("400x300")# geometry means height and width
#app heading
title = tk.Label(root, text="AI Sticker Maker", font=("Arial", 20))
title.pack(pady=40)#.pack adds component after another
#upload button
button = tk.Button(root, text="Upload image", command=create_sticker)#command is to show a certain command a button is supposed to do #if you do not back a certain component it will not show
button.pack(pady=20)#pady is the space between elements (measured in pixels)
#run the application
root.mainloop()