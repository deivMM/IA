import requests

api_key = "API_KEY" # Replace with your API key

url = "https://api.datacommons.org/v2/observation"


headers = {'Content-Type': 'application/json', 'X-API-Key': f'{api_key}'}

payload = {
    "select": ["entity","variable","date","value","facet"],
    "variable": {
        "dcids": ["Amount_EconomicActivity_GrossDomesticProduction_Nominal"]
    },
    "entity": {
        "dcids": ["country/COL"]
    }
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())