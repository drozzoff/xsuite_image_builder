import os
import subprocess
import sys

image_repo = os.environ['IMAGE_REPO']

if len(sys.argv) == 1:
	tag = f"{image_repo}:{os.environ['RECENT_MINOR_VERSION']}"

elif len(sys.argv) == 2:
	# allow to overwrite the tag manually
	tag = f"{image_repo}:{sys.argv[1]}" 
else:
	raise Exception("Too many parameters")

tag_exists = subprocess.run(
	["docker", "manifest", "inspect", tag],
	stdout = subprocess.DEVNULL,
	stderr = subprocess.DEVNULL
).returncode == 0

print(f"The tag '{tag}' exists = {tag_exists}")

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
	with open(github_output, "a") as f:
		f.write(f"tag_exists={'true' if tag_exists else 'false'}\n")