import sys
import subprocess
import os

env = os.environ.copy()
kicad_demo_path = ";C:\\Program Files\\KiCad\\7.0\\bin\\"
env['PATH'] += kicad_demo_path

try:
    print("kicad_cli version: ")
    kicad_cli_version = subprocess.run("kicad-cli --version", env=env, shell=True)
except FileNotFoundError:
    kicad_cli_version = subprocess.CompletedProcess
    kicad_cli_version.returncode = 1

assert kicad_cli_version.returncode == 0, "kicad-cli not found, please fix your path"
