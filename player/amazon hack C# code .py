

Copy
import requests
import string
import random

def generate_email():
    domain = "example.com"
    email = f"{generate_random_string(10)}@{domain}"
    response = requests.get(f"https://api.typer.ooo/check?email={email}").text

    if "valid" not in response.lower():
        return generate_email()

    return email

def generate_random_string(length):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
  
