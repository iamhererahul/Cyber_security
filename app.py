from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Pillow for image handling
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)  # Initialize a new window
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_message = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt_message)

    elif password == "":
        messagebox.showerror("Decryption", "Please enter the password")
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid password")

def encrypt():
    global screen1  # Declare screen1 as global to access it in the function
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)  # Initialize a new window
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt_message)

    elif password == "":
        messagebox.showerror("Encryption", "Please enter the password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")

    # Load the .webp image using PIL
    image_icon = Image.open("keys.webp")
    image_icon = ImageTk.PhotoImage(image_icon)  # Convert to PhotoImage compatible with Tkinter

    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)

    text1 = Text(screen, bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    text1.config(font=("Roboto", 20), bd=2)

    Label(text="Enter secret key for encryption and Decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
