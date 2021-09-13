import requests
response=requests.get('http://api.open-notify.org/astros.json')
json=response.json()
#print(json)
y=1
for x in json["people"]:
    print("Person #", y," in space is", x["name"]," and the craft name is", x["craft"])
    y=y+1
