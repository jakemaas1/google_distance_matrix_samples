import requests

api_key = 'KEY_HERE'
url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key={api_key}'

# GET request
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# JSON blob with distance, time between points
print(response.text)
