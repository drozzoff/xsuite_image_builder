import json, urllib.request
import os

url = "https://pypi.org/pypi/xsuite/json"
with urllib.request.urlopen(url) as r:
	data = json.load(r)

version = data["info"]["version"]

print(f"The most recent version on PyPi is '{version}'")

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
	with open(github_output, "a") as f:
		f.write(f"version={version}\n")