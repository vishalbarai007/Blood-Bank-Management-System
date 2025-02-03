import tkinter as tk
from tkinter import messagebox
import sqlite3

import requests

response = requests.get("http://127.0.0.1:8000/api/donors/")
print(response.json())


def save_donor():
    conn = sqlite3.connect("bloodbank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donor (name, age, blood_group, contact) VALUES (?, ?, ?, ?)",
                   (entry_name.get(), entry_age.get(), entry_blood.get(), entry_contact.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Donor added successfully")

root = tk.Tk()
root.title("Donor Registration")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Blood Group").pack()
entry_blood = tk.Entry(root)
entry_blood.pack()

tk.Label(root, text="Contact").pack()
entry_contact = tk.Entry(root)
entry_contact.pack()

tk.Button(root, text="Save Donor", command=save_donor).pack()

root.mainloop()
