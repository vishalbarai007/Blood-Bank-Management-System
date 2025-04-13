import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime
import os

# Backend API URL
API_BASE_URL = "http://127.0.0.1:8000/api/"

class BloodBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Bank Management System")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Set app icon and style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", background="#e74c3c", foreground="white", font=("Arial", 10, "bold"))
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"), foreground="#e74c3c")
        
        # User session data
        self.current_user = None
        
        # Create main container
        self.main_container = ttk.Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Start with login page
        self.show_login_page()
    
    def show_login_page(self):
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()
        
        # Create login frame
        login_frame = ttk.Frame(self.main_container, padding=20)
        login_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_label = ttk.Label(login_frame, text="Blood Bank Management System", style="Header.TLabel")
        header_label.pack(pady=20)
        
        # Login form
        form_frame = ttk.Frame(login_frame)
        form_frame.pack(pady=20)
        
        ttk.Label(form_frame, text="Username:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(form_frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(form_frame, text="Password:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.password_entry = ttk.Entry(form_frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        
        # Login button
        login_button = ttk.Button(form_frame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=20)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        try:
            response = requests.post(
                f"{API_BASE_URL}login/", 
                data={"username": username, "password": password}
            )
            
            if response.status_code == 200:
                self.current_user = response.json()
                self.show_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Error", "Could not connect to the server. Please make sure the Django server is running.")
    
    def show_dashboard(self):
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()
        
        # Create dashboard frame
        dashboard_frame = ttk.Frame(self.main_container)
        dashboard_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header with welcome message
        header_frame = ttk.Frame(dashboard_frame)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        welcome_label = ttk.Label(
            header_frame, 
            text=f"Welcome, {self.current_user['username']}!", 
            style="Header.TLabel"
        )
        welcome_label.pack(side=tk.LEFT)
        
        logout_button = ttk.Button(header_frame, text="Logout", command=self.logout)
        logout_button.pack(side=tk.RIGHT)
        
        # Navigation buttons
        nav_frame = ttk.Frame(dashboard_frame)
        nav_frame.pack(fill=tk.X, padx=10, pady=10)
        
        donor_button = ttk.Button(
            nav_frame, 
            text="Donor Registration", 
            command=self.show_donor_form
        )
        donor_button.pack(side=tk.LEFT, padx=5)
        
        stock_button = ttk.Button(
            nav_frame, 
            text="Blood Stock", 
            command=self.show_blood_stock
        )
        stock_button.pack(side=tk.LEFT, padx=5)
        
        contact_button = ttk.Button(
            nav_frame, 
            text="Contact Us", 
            command=self.show_contact_form
        )
        contact_button.pack(side=tk.LEFT, padx=5)
        
        # Content frame (initially empty)
        self.content_frame = ttk.Frame(dashboard_frame, padding=10)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Show blood stock by default
        self.show_blood_stock()
    
    def logout(self):
        self.current_user = None
        self.show_login_page()
    
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_donor_form(self):
        self.clear_content_frame()
        
        # Create donor registration form
        form_frame = ttk.Frame(self.content_frame)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(form_frame, text="Donor Registration", style="Header.TLabel").grid(
            row=0, column=0, columnspan=2, pady=10, sticky=tk.W
        )
        
        # Form fields
        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.donor_name = ttk.Entry(form_frame, width=30)
        self.donor_name.grid(row=1, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Age:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.donor_age = ttk.Entry(form_frame, width=30)
        self.donor_age.grid(row=2, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Blood Group:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.donor_blood_group = ttk.Combobox(
            form_frame, 
            values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
            width=28
        )
        self.donor_blood_group.grid(row=3, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Phone:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.donor_phone = ttk.Entry(form_frame, width=30)
        self.donor_phone.grid(row=4, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Email:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.donor_email = ttk.Entry(form_frame, width=30)
        self.donor_email.grid(row=5, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Address:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.donor_address = tk.Text(form_frame, width=30, height=4)
        self.donor_address.grid(row=6, column=1, pady=5, sticky=tk.W)
        
        # Submit button
        submit_button = ttk.Button(form_frame, text="Submit", command=self.submit_donor)
        submit_button.grid(row=7, column=0, columnspan=2, pady=20)
    
    def submit_donor(self):
        # Get form data
        name = self.donor_name.get()
        age = self.donor_age.get()
        blood_group = self.donor_blood_group.get()
        phone = self.donor_phone.get()
        email = self.donor_email.get()
        address = self.donor_address.get("1.0", tk.END).strip()
        
        # Validate form data
        if not all([name, age, blood_group, phone, email, address]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            age = int(age)
            if age < 18 or age > 65:
                messagebox.showerror("Error", "Age must be between 18 and 65")
                return
        except ValueError:
            messagebox.showerror("Error", "Age must be a number")
            return
        
        # Prepare data for API
        donor_data = {
            "name": name,
            "age": age,
            "blood_group": blood_group,
            "phone": phone,
            "email": email,
            "address": address
        }
        
        try:
            # Send data to API
            response = requests.post(
                f"{API_BASE_URL}donors/", 
                json=donor_data,
                auth=(self.current_user['username'], 'admin123')  # In a real app, you'd store the password or use tokens
            )
            
            if response.status_code == 201:
                messagebox.showinfo("Success", "Donor registered successfully")
                # Clear form
                self.donor_name.delete(0, tk.END)
                self.donor_age.delete(0, tk.END)
                self.donor_blood_group.set("")
                self.donor_phone.delete(0, tk.END)
                self.donor_email.delete(0, tk.END)
                self.donor_address.delete("1.0", tk.END)
                # Refresh blood stock
                self.show_blood_stock()
            else:
                messagebox.showerror("Error", f"Failed to register donor: {response.text}")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Error", "Could not connect to the server")
    
    def show_blood_stock(self):
        self.clear_content_frame()
        
        # Create blood stock display
        stock_frame = ttk.Frame(self.content_frame)
        stock_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(stock_frame, text="Blood Stock", style="Header.TLabel").pack(pady=10, anchor=tk.W)
        
        # Create treeview for blood stock
        columns = ("Blood Group", "Quantity", "Last Updated")
        tree = ttk.Treeview(stock_frame, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)
        
        # Add a scrollbar
        scrollbar = ttk.Scrollbar(stock_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)
        
        try:
            # Fetch blood stock data from API
            response = requests.get(
                f"{API_BASE_URL}blood-stock/",
                auth=(self.current_user['username'], 'admin123')  # In a real app, you'd store the password or use tokens
            )
            
            if response.status_code == 200:
                stock_data = response.json()
                
                # Clear existing data
                for item in tree.get_children():
                    tree.delete(item)
                
                # Insert new data
                for item in stock_data:
                    last_updated = datetime.fromisoformat(item['last_updated'].replace('Z', '+00:00'))
                    formatted_date = last_updated.strftime("%Y-%m-%d %H:%M")
                    tree.insert("", tk.END, values=(item['blood_group'], item['quantity'], formatted_date))
            else:
                messagebox.showerror("Error", f"Failed to fetch blood stock: {response.text}")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Error", "Could not connect to the server")
        
        # Add refresh button
        refresh_button = ttk.Button(stock_frame, text="Refresh", command=self.show_blood_stock)
        refresh_button.pack(pady=10)
    
    def show_contact_form(self):
        self.clear_content_frame()
        
        # Create contact form
        form_frame = ttk.Frame(self.content_frame)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(form_frame, text="Contact Us", style="Header.TLabel").grid(
            row=0, column=0, columnspan=2, pady=10, sticky=tk.W
        )
        
        # Form fields
        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.contact_name = ttk.Entry(form_frame, width=30)
        self.contact_name.grid(row=1, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.contact_email = ttk.Entry(form_frame, width=30)
        self.contact_email.grid(row=2, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Subject:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.contact_subject = ttk.Entry(form_frame, width=30)
        self.contact_subject.grid(row=3, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(form_frame, text="Message:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.contact_message = tk.Text(form_frame, width=30, height=6)
        self.contact_message.grid(row=4, column=1, pady=5, sticky=tk.W)
        
        # Submit button
        submit_button = ttk.Button(form_frame, text="Submit", command=self.submit_contact)
        submit_button.grid(row=5, column=0, columnspan=2, pady=20)
    
    def submit_contact(self):
        # Get form data
        name = self.contact_name.get()
        email = self.contact_email.get()
        subject = self.contact_subject.get()
        message = self.contact_message.get("1.0", tk.END).strip()
        
        # Validate form data
        if not all([name, email, subject, message]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Prepare data for API
        contact_data = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }
        
        try:
            # Send data to API
            response = requests.post(f"{API_BASE_URL}contacts/", json=contact_data)
            
            if response.status_code == 201:
                messagebox.showinfo("Success", "Message sent successfully")
                # Clear form
                self.contact_name.delete(0, tk.END)
                self.contact_email.delete(0, tk.END)
                self.contact_subject.delete(0, tk.END)
                self.contact_message.delete("1.0", tk.END)
            else:
                messagebox.showerror("Error", f"Failed to send message: {response.text}")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Error", "Could not connect to the server")

if __name__ == "__main__":
    root = tk.Tk()
    app = BloodBankApp(root)
    root.mainloop()