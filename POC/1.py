import tkinter as tk
from tkinter import messagebox
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot


def decrypt_message():
    try:
        e = int(e_entry.get())
        d = int(d_entry.get())
        c = int(c_entry.get())
        # Your decryption logic goes here
        # ...
        # Display the result
        messagebox.showinfo("Decrypted Message",
                            "Your decrypted message is: " + str(message))
    except Exception as ex:
        messagebox.showerror("Error", "An error occurred: " + str(ex))


# Create the main window
window = tk.Tk()
window.title("RSA Decryption Tool")

# Create and add widgets (Entry fields, Labels, Button)
e_label = tk.Label(window, text="Enter e:")
e_label.pack()
e_entry = tk.Entry(window)
e_entry.pack()

d_label = tk.Label(window, text="Enter d:")
d_label.pack()
d_entry = tk.Entry(window)
d_entry.pack()

c_label = tk.Label(window, text="Enter c:")
c_label.pack()
c_entry = tk.Entry(window)
c_entry.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message)
decrypt_button.pack()

# Start the application
window.mainloop()
