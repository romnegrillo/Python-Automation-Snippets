import urllib.request

with urllib.request.urlopen("http://data.pr4e.org/romeo.txt") as f:
    bytes_received = f.read() 

    # Convert bytes to string by decoding it.
    data = bytes_received.decode()
    print(data)

    # Convert it to list of words by splitting between spaces.
    data = data.split()

    # Loop through words and add its occurences using a dictionary.
    words_dict = {}

    for word in data:
        words_dict[word] = words_dict.get(word, 0) + 1

    # Print the words and its occurence.
    for word, occurence in words_dict.items():
        print("{} occured {} times.".format(word, occurence))