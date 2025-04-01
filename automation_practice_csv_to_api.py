import csv
import requests

# URL of a mock API endpoint for testing
API_URL = "https://jsonplaceholder.typicode.com/users"

def send_contact(contact):
    # Combine first and last names into a full name
    name = f"{contact['first_name']} {contact['last_name']}"
    email = contact['email']
    
    # Create a payload to send to the API
    payload = {
        "name": name,
        "email": email
    }
    
    # Send the POST request
    response = requests.post(API_URL, json=payload)
    print(f"Sent {name} with status code: {response.status_code}")

def main():
    csv_filename = "contacts.csv"  # Ensure this file is in the same folder
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            send_contact(row)

if __name__ == "__main__":
    main()
