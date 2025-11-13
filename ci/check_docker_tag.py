import os
import subprocess

image_repo = os.environ['IMAGE_REPO']
recent_minor_version = os.environ['RECENT_MINOR_VERSION']
tag = f"{image_repo}:{recent_minor_version}"

tag_exists = subprocess.run(
	["docker", "manifest", "inspect", tag],
	stdout = subprocess.DEVNULL,
	stderr = subprocess.DEVNULL
).returncode == 0

print(f"The version '{tag}' exists = {tag_exists}")

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
	with open(github_output, "a") as f:
		f.write(f"tag_exists={'true' if tag_exists else 'false'}\n")