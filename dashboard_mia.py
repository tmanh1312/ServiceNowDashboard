from flask import Flask, render_template
import requests
from datetime import datetime
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Replace these with your ServiceNow API details
SERVICE_NOW_API_URL = 'https://uw.service-now.com/api/now/table/u_simple_requests'
username = ''
password = ''

def test_service_now_api(username, password):
    # Construct query parameters
    # Construct query parameters
    query_params = {
    'sysparm_query': 'active=true^assignment_group=1854c1a06f1ca100ab448bec5d3ee4ef^ORassignment_group=6c54c1a06f1ca100ab448bec5d3ee4f2^ORassignment_group=6bbb84d16ff5650090ead2054b3ee414^ORassignment_group=386e43f06fb1f1041b9fa7131c3ee497^ORassignment_group=a7765209db469308448a7f8cbf9619e4^state!=6^state!=3^state!=7',
    'sysparm_display_value': 'false',
    'sysparm_exclude_reference_link': 'false',
    'sysparm_fields': 'number, sys_created_on',  # Use square brackets for a list
    'sysparm_limit': '100'
    }

    # Make API call with Basic Authentication
    try:
        response = requests.get(SERVICE_NOW_API_URL, params=query_params, auth=HTTPBasicAuth(username, password))
        
        # Check the response
        if response.status_code == 200:
            print("API call successful!")

            # Assuming you want to do something with the response data
            tickets_data = response.json().get('result', [])
            print(tickets_data)

            # Example: Calculate total tickets
            total_tickets = len(tickets_data)
            print(f'Total Tickets: {total_tickets}')

            return tickets_data  # Return the data if needed
        else:
            print(f'Error {response.status_code}: {response.text}')
            return None
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None

def get_tickets_count():
    # Call the test_service_now_api function with credentials
    tickets_data = test_service_now_api(username, password)

    if tickets_data is not None:
        # Process the tickets_data as needed
        # Example: Count the number of tickets
        ticket_count = len(tickets_data)
        return tickets_data,ticket_count
    else:
        return None

@app.route('/')
def dashboard():
    ticket_count = get_tickets_count()
    if ticket_count is not None:
        return render_template('dashboard.html', ticket_count=ticket_count)
    else:
        return 'Error fetching data from ServiceNow API'

if __name__ == '__main__':
    app.run(debug=True)
