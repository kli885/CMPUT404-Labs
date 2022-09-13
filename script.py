import requests

# Gets the current version of requests package
version = requests.__version__

# Gets the google Homepage
google = requests.get("https://www.google.com")
