"""
automatically checks for kicad_cli availability
"""
import sys
import subprocess
import os

def check_for_kicad():
    env = os.environ.copy()
    # kicad_demo_path = ";C:\\Program Files\\KiCad\\7.0\\bin\\"
    # env['PATH'] += kicad_demo_path

    try:

        kicad_cli_version_out = subprocess.run("kicad-cli --version", env=env, shell=True, stdout = subprocess.PIPE)
        print("kicad_cli version:", kicad_cli_version_out.stdout.decode('utf-8'))
    except FileNotFoundError:
        kicad_cli_version_out = subprocess.CompletedProcess
        kicad_cli_version_out.returncode = 1

    assert kicad_cli_version_out.returncode == 0, "kicad-cli not found, please fix your path"
