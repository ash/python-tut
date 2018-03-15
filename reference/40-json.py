import json

data = [1, 2, {'key': "value"}]

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json') as f:
    data1 = json.load(f)
    print(data1)