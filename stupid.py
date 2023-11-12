import requests
import json


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    quote = response.text
    print('wow what genius:', quote)
    return quote


def append_file():
    quote = get_quote()

    with open("stupidass-file.txt", "a") as stupid_smell:
        stupid_smell.write(f"{quote}\n")

append_file()
