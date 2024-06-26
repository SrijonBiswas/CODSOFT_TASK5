import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            return False
        self.contacts[name] = {'phone': phone, 'email': email}
        return True

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def update_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def list_contacts(self):
        return self.contacts


class ContactBookApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = ContactBook()

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0)

        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=2, column=0)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=3, column=1)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=4, column=0)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if self.contact_book.add_contact(name, phone, email):
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Contact already exists!")

    def view_contacts(self):
        contacts = self.contact_book.list_contacts()
        contact_list = "\n".join([f"{name}: {info['phone']}, {info['email']}" for name, info in contacts.items()])
        messagebox.showinfo("Contact List", contact_list if contact_list else "No contacts available.")

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.contact_book.get_contact(name)
        if contact:
            messagebox.showinfo("Contact Found", f"{name}: {contact['phone']}, {contact['email']}")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if self.contact_book.update_contact(name, phone, email):
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        name = self.name_entry.get()
        if self.contact_book.delete_contact(name):
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")


if __name__ == "_main_":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()