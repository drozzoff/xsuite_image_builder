import os
import subprocess

image_repo = os.environ['IMAGE_REPO']
recent_xsuite_version = os.environ['RECENT_XSUITE_VERSION']
tag = f"{image_repo}:{recent_xsuite_version}"

# ingoring patches, only minor tags
parts = recent_xsuite_version.split(".")
if len(parts) >= 2:
    minor_tag = ".".join(parts[:2])
else:
    minor_tag = recent_xsuite_version

tag_exists = subprocess.run(
	["docker", "manifest", "inspect", minor_tag],
	stdout = subprocess.DEVNULL,
	stderr = subprocess.DEVNULL
).returncode == 0

print(f"The latest `xsuite` recent version is {recent_xsuite_version}")
print(f"The latest minor release '{minor_tag}' exists = {tag_exists}")

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
	with open(github_output, "a") as f:
		f.write(f"tag_exists={'true' if tag_exists else 'false'}\n")