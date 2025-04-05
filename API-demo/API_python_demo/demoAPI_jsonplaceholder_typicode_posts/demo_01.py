import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

api_txt_file = "demoAPI_jsonplaceholder_typicode_posts.txt"
with open(api_txt_file, 'a') as txt_file:
    json.dump(data, txt_file, indent=4)
    txt_file.write('\n')
    
api_json_file = "posts.json"
with open(api_json_file,'a') as json_file:
    json.dump(data, json_file, indent=4)