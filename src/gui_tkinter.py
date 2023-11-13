import tkinter as tk
from tkinter import ttk

from dpi import set_dpi_awareness
set_dpi_awareness()

# def get_user_entry():
#     searchfield = user_text.get()
#     print(searchfield)

root = tk.Tk()   # Tkinter window
root.title("Movies")   # Name
root.geometry("1000x600")   # Window resolution
root.resizable(True, True)  # Window size is adjustable, on width and height
root.config(background="orange")   # Change background color
root.iconbitmap("src/gui_images/Movies.ico")   # Icon image
user_input = tk.StringVar()


def print_value():
   print(user_input.get())


app_label = tk.Label(root, text="Movies Recommendation App", font=("Calibri", 24), background="orange")
app_label.pack()   # pack() is the geometry manager

photo = tk.PhotoImage(file="src/gui_images/Movies_256x256.png")   # The image object to be passed to the ttk object
image_label = ttk.Label(root, image=photo, padding=3)   # The Label image object
image_label.pack()

# text_label = ttk.Label(root, text="Search for a movie", font=("Calibri", 18), background="orange")   # The Label text object
# text_label.pack(side=tk.LEFT, padx=30, pady=100)

text = ttk.Entry(root, width=20, textvariable=user_input)  # Creates the text box, with height = 3 lines
button = ttk.Button(root,
                    text="Search results",
                    command=print_value)


# user_text = tk.Text(root, height=1, width=40)   # Search field
# user_text.pack(side=tk.RIGHT, padx=30, pady=10)

text.pack()  #place, pentru a muta search field
button.pack(ipadx=10, ipady=10, expand=True)

#button = tk.Button(root,
#                   text="Search results",
#                   font=("Calibri", 16),
#                   activebackground= "gray",
#                   activeforeground= "yellow",
#                   )   # The search button  "command= get_user_entry" The command that will give a button functionality
#button.pack(padx=30, pady=30)



# app_label = tk.Label(root, text="Search for a movie name: ", font=("Calibri", 20))
# app_label.pack(side=tk.LEFT)


root.mainloop()