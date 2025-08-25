import re

url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#username = url.replace("https://", "")
#username = url.removeprefix("https://")

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)§", url, re.IGNORECASE):
    print(f"Username:", matches.groups(1))

