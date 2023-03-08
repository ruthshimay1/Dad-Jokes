import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'applications/json'})

print( 'Your dad joke: {0}'.format(response.json()['joke']))

input("Press Enter to continue!")
