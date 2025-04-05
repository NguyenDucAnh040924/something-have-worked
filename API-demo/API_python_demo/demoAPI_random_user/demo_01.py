import requests
import json

url = "https://randomuser.me/api/"

respone = requests.get(url)

# if requests.status_codes == 200:
#     print(requests.json())
# else:
#     print(f"Error: {respone.status_code}")

data = respone.json()

with open('demoAPI_random_user.txt', 'a') as file:
    json.dump(data,file, indent=4)
    file.write('\n')


    