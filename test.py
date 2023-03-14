import concurrent.futures
import requests

# Define the API endpoints to call
api_endpoints = [
    'http://192.168.211.90:8000/port-scan?ip_address=192.168.252.28 ',
    'http://192.168.211.90:8000/vulnerabilities/192.168.252.28%20',
    'http://192.168.211.90:8000/phishing?ip_address=192.168.252.28%20',
    
]

# Define a function to call the APIs
def call_api(api_endpoint):
    response = requests.get(api_endpoint)
    return response.json()

# Create a ThreadPoolExecutor with 3 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit the API calls to the executor
    futures = {executor.submit(call_api, endpoint): endpoint for endpoint in api_endpoints}

    # Wait for all the API calls to complete and retrieve the results
    for future in concurrent.futures.as_completed(futures):
        endpoint = futures[future]
        try:
            result = future.result()
            print(result)
        except Exception as exc:
            print(f'{endpoint} generated an exception: {exc}')
        else:
            print(f'{endpoint} returned: {result}')
    
    # Process the API results as needed
