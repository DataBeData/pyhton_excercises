
import re

name = input("what's yourname? ").strip()

if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2).strip() + " " + matches.group(1).strip()
   
print(f"Hello, {name}")

'''last, first = matches.groups()
    name = f"{first} {last}"
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"'''

'''if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")'''
