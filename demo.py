from flask import Flask, request, jsonify, render_template_string
from faker import Faker
from faker.providers import internet
import csv

app = Flask(__name__)

fake = Faker()
fake.add_provider(internet)

@app.route('/', methods=['GET'])
def index():
    return open('index.html', 'r').read()

@app.route('/generate_data', methods=['POST'])
def generate_data():
    num_users = int(request.json['numUsers'])
    user_data = generate_user_data(num_users)
    html_table = generate_html_table(user_data)
    return html_table

def generate_user_data(num_users):
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
    return user_data

def generate_html_table(user_data):
    html_table = '<table><tr>'
    for key in user_data[0].keys():
        html_table += f'<th>{key}</th>'
    html_table += '</tr>'
    for user in user_data:
        html_table += '<tr>'
        for value in user.values():
            html_table += f'<td>{value}</td>'
        html_table += '</tr>'
    html_table += '</table>'
    return html_table

if __name__ == '__main__':
    app.run(debug=True)