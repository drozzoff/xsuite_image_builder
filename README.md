Checks "PyPi" daily for a new version of `xsuite` and builds+pushes a new Docker image if a new version is found.

I store them at `drozzoff/xsuite:latest` on Docker Hub.

The versions stored there:
- `:{version}` - Bare version.
- `:{version}-opencl` - with `pyopencl`.
- `:{version}-gsihpc` - for the use on GSI HPC.