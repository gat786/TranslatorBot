import json

with open("countries.json", "r") as data:
    json_data = json.loads(data.read())

with open("required_data.json", "w") as required:
    for every in json_data:
        name = every["name"]
        currency = every["currencies"]
        capital = every["capital"]
        languages = every["languages"]
        emoji_flag = every["flag"]
        data = {"name":name,"currency":currency,"capital":capital,"languages":languages,"flag":emoji_flag}
        json.dump(data,required)

