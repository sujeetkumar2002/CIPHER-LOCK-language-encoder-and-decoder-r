from tkinter import *
import pybase64 
from tkinter import messagebox

root = Tk()
root.title("Cipher Lock")
root.geometry("500x400")
root.config(bg="lime green")


def reset():

    my_text.delete(1.0, END)
    my_entry.delete(0, END)


def encrypt():
  
    secret = my_text.get(1.0, END)
   
    my_text.delete(1.0, END)

    # Logic for password
    if my_entry.get() == "123456789":
        # Convert to byte
        secret = secret.encode("ascii")
        # Convert to base64
        secret = pybase64.b64encode(secret)
        # Convert it back to ascii
        secret = secret.decode("ascii")
        # Print to text box
        my_text.insert(END, secret)

    else:
        # Flash a message if wrong password
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!")


def decrypt():
    # Get text from text box
    secret = my_text.get(1.0, END)
    # Clear the screen
    my_text.delete(1.0, END)

    # Logic for password
    if my_entry.get() == "123456789":
        # Convert to byte
        secret = secret.encode("ascii")
        # Convert to base64
        secret = pybase64.b64decode(secret)
        # Convert it back to ascii
        secret = secret.decode("ascii")
        # Print to text box
        my_text.insert(END, secret)

    else:
        # Flash a message if wrong password
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!")


my_frame = Frame(root)
my_frame.pack(pady=20)

enc_button = Button(my_frame, text="Encrypt", font=("Helvetica", 18), command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = Button(my_frame, text="Decrypt", font=("Helvetica", 18), command=decrypt)
dec_button.grid(row=0, column=1, padx=20)

reset_button = Button(my_frame, text="Reset", font=("Helvetica", 18), command=reset)
reset_button.grid(row=0, column=2)

enc_label = Label(root, text="Cipher Lock: Encryption and Decryption Tool", font=("Helvetica", 14))
enc_label.pack()

my_text = Text(root, width=57, height=10)
my_text.pack(pady=10)

Code_label = Label(root, text="Enter Your Code", font=("Helvetica", 14))
Code_label.pack()

my_entry = Entry(root, font=("Helvetica", 18), width=35, show="*")
my_entry.pack(pady=10)

root.mainloop()