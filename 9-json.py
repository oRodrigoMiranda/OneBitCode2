import json

# 1 - strings para dicionarios
person = '{"name":"Rodrigo", "languages":["javascript","python"]}'
person_dict = json.loads(person)
print(person_dict)

# 2 - Dicionarios para json
person_json = json.dumps(person_dict)
print(person_json)

# 3 - Formatando um json
print(json.dumps(person_dict, indent = 4, sort_keys=True))

#4 - Salvando Json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)

#5 - Lendo Json externo
with open("iris.json", "r") as f:
    data = json.load(f)
    json.dumps(data)
    for x in data:
        print (x.keys())
    
