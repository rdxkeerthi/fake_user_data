import tkinter as tk
from tkinter import filedialog
from faker import Faker
from faker.providers import internet
import csv

class UserDataGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("User Data Generator")

        # Create input field for number of users
        self.num_users_label = tk.Label(root, text="Number of users:")
        self.num_users_label.pack()
        self.num_users_entry = tk.Entry(root)
        self.num_users_entry.pack()

        # Create button to generate user data
        self.generate_button = tk.Button(root, text="Generate User Data", command=self.generate_user_data)
        self.generate_button.pack()

        # Create label to display status
        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def generate_user_data(self):
        # Get number of users from input field
        num_users = int(self.num_users_entry.get())

        # Generate user data
        fake = Faker()
        fake.add_provider(internet)
        user_data = []
        for _ in range(num_users):
            user = {
                'Name': fake.name(),
                'Email': fake.free_email(),
                'Phone Number': fake.phone_number(),
                'Birthdate': fake.date_of_birth(),
                'Address': fake.address(),
                'City': fake.city(),
                'Country': fake.country(),
                'ZIP Code': fake.zipcode(),
                'Job Title': fake.job(),
                'Company': fake.company(),
                'IP Address': fake.ipv4_private(),
                'Credit Card Number': fake.credit_card_number(),
                'Username': fake.user_name(),
                'Website': fake.url(),
                'SSN': fake.ssn()
            }
            user_data.append(user)

        # Save user data to CSV file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv")
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = [
                "Name",
                "Email",
                "Phone Number",
                "Birthdate",
                "Address",
                "City",
                "Country",
                "ZIP Code",
                "Job Title",
                "Company",
                "IP Address",
                "Credit Card Number",
                "Username",
                "Website",
                "SSN"
            ]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(user_data)

        # Update status label
        self.status_label.config(text=f"User data generated and saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserDataGenerator(root)
    root.mainloop()