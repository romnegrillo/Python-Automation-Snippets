import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:

    # Connect to the host at port 80 (http).
    f.connect(("data.pr4e.org", 80))

    cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
    f.send(cmd)

    # To hold the bytes received.
    data = ""

    while True:
        bytes_received = f.recv(512)

        # Stop if no bytes received, meaning it ended.
        if len(bytes_received) < 1:
            break
        
        data += bytes_received.decode()
    
    # If data variable has contents, we print 
    # and get its word occurence via dictionary.
    if len(data):

        print(data)
 
        words_dict = {}

        # Split the string into list of words.
        data = data.split()

        for word in data:
            words_dict[word] = words_dict.get(word, 0) + 1

    # Print the dictionary items.
    for word, occurence in words_dict.items():
        print("{} occured {} times.".format(word, occurence))


       