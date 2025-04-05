import json

def read_file_json(ten_file):

    with open(ten_file, 'r') as file:

        data = json.load(file)

        for item in data:
            print(f"{item["userId"]}, {item["id"]}, {item["title"]}, {item["body"]}\n")