import requests
from requests.auth import HTTPBasicAuth

def test_service_now_api(username, password):
    # Replace 'your_instance_url' with your ServiceNow instance URL
    api_url = 'https://uw.service-now.com/api/now/table/u_simple_requests'
    
    # Construct query parameters
    query_params = {
    'sysparm_query': 'active=true^assignment_group=1854c1a06f1ca100ab448bec5d3ee4ef^ORassignment_group=6c54c1a06f1ca100ab448bec5d3ee4f2^ORassignment_group=6bbb84d16ff5650090ead2054b3ee414^ORassignment_group=386e43f06fb1f1041b9fa7131c3ee497^ORassignment_group=a7765209db469308448a7f8cbf9619e4^state!=6^state!=3^state!=7',
    'sysparm_display_value': 'false',
    'sysparm_exclude_reference_link': 'false',
    'sysparm_fields': 'number, sys_created_on',  # Use square brackets for a list
    'sysparm_limit': '100'
    }
    
    # Construct headers with API name
    headers = {
        'X-Api-Name': username 
    }

    # Make API call with Basic Authentication
    try:
        response = requests.get(api_url, params=query_params, headers=headers, auth=HTTPBasicAuth(username, password))
        
        # Check the response
        if response.status_code == 200:
            print("API call successful!")

            # Count tickets with 'REQ%' identifier
            tickets_data = response.json().get('result', [])
            print(tickets_data)
            #req_tickets = [ticket for ticket in tickets_data if 'REQ%' in ticket.get('number', '')]
            #print(req_tickets)

            # Calculate total tickets
            total_tickets = len(tickets_data)
            print(f'Total Tickets: {total_tickets}')
        else:
            print(f'Error {response.status_code}: {response.text}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Example usage:
test_service_now_api(username='', password='')
