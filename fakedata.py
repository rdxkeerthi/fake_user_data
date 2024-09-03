# Import necessary libraries and modules.
from faker import Faker
from faker.providers import internet
import csv

# Function to generate user data with the specified number of users
def generate_user_data(num_of_users):
  # Create a Faker instance.
  fake = Faker()
  # Add the Internet provider to generate email addresses
  fake.add_provider(internet)
  # Initialize an empty list to store user data
  user_data = []
  # Loop to generate data for the specified number of users
  for _ in range(num_of_users):
    # Create a dictionary representing a user
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
    # Append the user data dictionary to the list
    user_data.append(user)
  # Return the list of user data
  return user_data

# Example usage:
# Generate user data for 10 users
user_data = generate_user_data(100)
# Print the generated user data
print(user_data)
# Write the user data to a CSV file
with open('user_data.csv', 'w', newline='') as csvfile:
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