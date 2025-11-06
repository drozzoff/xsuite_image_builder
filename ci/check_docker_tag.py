import os
import subprocess

image_repo = os.environ['IMAGE_REPO']
recent_xsuite_version = os.environ['RECENT_XSUITE_VERSION']
tag = f"{image_repo}:{recent_xsuite_version}"

tag_exists = subprocess.run(
	["docker", "manifest", "inspect", tag],
	stdout = subprocess.DEVNULL,
	stderr = subprocess.DEVNULL
).returncode == 0

print(f"The image with the version '{recent_xsuite_version}' exists = {tag_exists}")

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
	with open(github_output, "a") as f:
		f.write(f"tag_exists={'true' if tag_exists else 'false'}\n")