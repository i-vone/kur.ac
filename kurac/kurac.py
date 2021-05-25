import requests

def kurac(url, prefix=""): # Define main function
    r = requests.post("http://www.kur.ac/_generate", data={"url": url, "subdomain": prefix}) # Make request to kur.ac containing the URL and desired subdomain.
    return r.json()["url"] # Return the shortened URL
