import paddlex
import importlib.metadata
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True)
parser.add_argument('--nvidia', action='store_true')

args = parser.parse_args()

user_deps = [dist.metadata["Name"] for dist in importlib.metadata.distributions()]
deps_all = list(paddlex.utils.deps.BASE_DEP_SPECS.keys())
deps_need = [dep for dep in user_deps if dep in deps_all]

cmd = [
    "pyinstaller",
    args.file,
    "--collect-data", "paddlex",
    "--collect-binaries", "paddle"
]

if args.nvidia:
    cmd += ["--collect-binaries", "nvidia"]

for dep in deps_need:
    cmd += ["--copy-metadata", dep]

subprocess.run(cmd)
