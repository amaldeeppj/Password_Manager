from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=400, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(240, 100, image=lock_img)
canvas.grid(row=0, column=0, padx=50, columnspan=5)

l1 = Label(text="Website", bg="white")
l1.grid(row=1, column=1)

l2 = Label(text="Email/Username", bg="white")
l2.grid(row=2, column=1)

l3 = Label(text="Password", bg="white")
l3.grid(row=3, column=1)

e1 = Entry(borderwidth=3, width=40)
e1.focus()
e1.grid(row=1, column=2, columnspan=3, sticky="W")

e2 = Entry(borderwidth=3, width=40)
e2.grid(row=2, column=2, columnspan=3, sticky="W")

e3 = Entry(borderwidth=3, width=40)
e3.grid(row=3, column=2, columnspan=2, sticky="W")

b1 = Button(text="Generate", padx=12, pady=0, activeforeground="blue", activebackground="grey", highlightthickness=0)
b1.grid(row=3, column=4, sticky="W")

b2 = Button(text="Add", activeforeground="blue", activebackground="grey", padx=106, borderwidth=3)
b2.grid(row=4, column=2, columnspan=3, sticky="W")


window.mainloop()

