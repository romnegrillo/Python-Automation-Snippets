import urllib.request, urllib.parse
import json

base_url = "http://py4e-data.dr-chuck.net/json?"

while True:
    location = input("Enter location: ")

    url = base_url + urllib.parse.urlencode({"address": location, "key":42})

    with urllib.request.urlopen(url) as f:
        print("Retrieving {}".format(url))

        data = f.read().decode()

        print("Retrieved {}".format(len(data)))

        json_data = json.loads(data)

        if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
                print('==== Failure To Retrieve ====')
                print(data)
                continue

        #print(json.dumps(json_data, indent=4))

        place_id = json_data["results"][0]["place_id"]

        print("Place id {}".format(place_id))



        