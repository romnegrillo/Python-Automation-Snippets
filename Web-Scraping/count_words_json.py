import urllib.request
import json

url = input("Enter location: ")

with urllib.request.urlopen(url) as f:
    print("Retrieving {}".format(url))

    data = f.read().decode()

    print("Retrieved {} characters".format(len(data)))

    json_data = json.loads(data)
    #print(json.dumps(json_data, indent=1))

    comment_count = len(json_data["comments"])
    count_sum = sum([i["count"] for i in json_data["comments"]])

    print("Count: {}".format(comment_count))
    print("Sum: {}".format(count_sum))




