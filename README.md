# User Data Generator

A Python script that generates fake user data and writes it to a CSV file.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Usage](#usage)
* [Code Explanation](#code-explanation)
* [Example Output](#example-output)
* [License](#license)

## Features

* Generates fake user data for a specified number of users
* Includes various fields such as name, email, phone number, birthdate, address, job title, company, IP address, credit card number, username, website, and SSN
* Writes the generated data to a CSV file

## Requirements

* Python 3.x
* Faker library (`pip install faker`)
* csv library (built-in)

## Usage

1. Clone the repository: `git clone https://github.com/rdxkeerthi/fake_user_data.git`
2. Install the required libraries: `pip install faker`
3. Run the script: `python3 fakedata.py`
4. Specify the number of users you want to generate data for (e.g., `python generate_user_data.py 100`)

## Code Explanation

The script uses the Faker library to generate fake user data. It defines a function `generate_user_data` that takes the number of users as an argument and returns a list of dictionaries, where each dictionary represents a user. The script then writes the generated data to a CSV file using the csv library.

## Example Output

The script generates a CSV file named `user_data.csv` with the following columns:

| Name | Email | Phone Number | Birthdate | Address | City | Country | ZIP Code | Job Title | Company | IP Address | Credit Card Number | Username | Website | SSN |
| ---| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Each row represents a user, with fake data generated for each column.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
