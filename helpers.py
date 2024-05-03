import requests

def get_event(year, month, day):
    api_url = 'https://api.api-ninjas.com/v1/historicalevents'
    params = {'year': year, 'month': month, 'day': day}
    headers = {'X-Api-Key': 'Ylmo+ck8sJ95RHi0jK9xJA==55Ug9GaJJSNcoyS5'}

    response = requests.get(api_url, params=params, headers=headers)

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
