import requests

def is_connected():
    """
    This function sends a get request to google.com and returns True
    if it succeeded which means we are connected, False otherwise.
    """
    try:
        url = "https://www.google.com"
        response = requests.get(url)

        print("We are connected to the internet.")
        print("{} returned a status code of {}".format(url, response.status_code))

        return True
    except Exception as exp:
        print("We are not connected to internet.")
        print("{} returned a status code of {}".format(url, response.status_code))
        print(str(exp))

    return False

def get_webpage(url):
    """
    This function prints the contents of the webpage as bytes
    specified in the URL by GET request. 
    Returns response status code of the operation.
    """
    if is_connected():
        response = requests.get(url)
        return response.content

def get_weboage_params(url, data):
    """
    This function adds the parameters in url of the web page then
    sends a GET request.  
    Returns response status code of the operation.
    """
    if is_connected():
        response = requests.get(url, data)
        print(response.url)
        return response.content

def post_webpage(url, data):
    """
    This function adds the key-value parameter as POST request in the web page.
    Returns response status code of the operation.
    """
    if is_connected():
        response = requests.post(url, data = data)
        print(response.url)
        return response.status_code


def main():
    url = "https://www.google.com"
    data = {"q":"rom negrillo"}

    print(get_webpage(url))
    print(get_weboage_params(url, data))
    print(post_webpage, data)

if __name__ == "__main__":
    main()
