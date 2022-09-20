import requests

# Gets the current version of requests package
version = requests.__version__

# Gets the google Homepage
google = requests.get("https://www.google.com")

# Gets the prints the script.py file uploaded on Github
github = requests.get(
    "https://raw.githubusercontent.com/kli885/CMPUT404-Labs/main/Lab1/script.py"
)
print(github.text)
