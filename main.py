import requests
import re

file_name = input("Enter the name of the file\n")
url = input("Enter the URL\n")

source = requests.get(url).text

list_url = re.findall(r"https?:?[\w/\-?=%.]+\.[\w/\-&?=%.]+", source)

with open(f"{file_name}.txt", "w") as file:
    for i in range(len(list_url)):
        file.write(f"{list_url[i]} \n")

print("Successfully recorded in a file!")