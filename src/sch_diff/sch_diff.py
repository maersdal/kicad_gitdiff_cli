import base64
import os
import pathlib
import random
import subprocess
import sys
import shutil
import webbrowser
import pkg_resources

import checkers  # runs a check for kicad-cli
import kicad_export.export_circuit_for_diff as kexport
import re

from svg_diff.svg_difftool import kdiff_svg


# https://git-scm.com/docs/git/2.18.0#Documentation/git.txt-codeGITEXTERNALDIFFcode
# diff for *.kicad_svg files?

def rand_short(a: int, b: int) -> str:
    return base64.b64encode(str(a + b + random.randint(0, 0xffffff)).encode('utf-8')).decode('utf-8').strip("=")


def diff_():
    """Used for calling from `git diff` with kicad_sch files
    calling convention documented at https://git-scm.com/docs/git/2.18.0#Documentation/git.txt-codeGITEXTERNALDIFFcode
    creates svg files in a temporary folder
    opens the visual diff in the browser.
    """
    print("SVG-based differ for kicad schematic files version", pkg_resources.get_distribution("kicad_gitdiff").version)
    path, old_file, old_hex, old_mode, new_file, new_hex, new_mode = sys.argv[1:]
    print("parameters")
    print(path, old_file, old_hex, old_mode, new_file, new_hex, new_mode)

    files = [pathlib.Path(old_file).resolve(), pathlib.Path(new_file).resolve()]
    assert os.path.splitext(files[0])[1] == ".kicad_sch"
    assert os.path.splitext(files[1])[1] == ".kicad_sch"
    ofolder = pathlib.Path(files[0].parent,
                           rand_short(int(old_hex[:6],16), int(new_hex[:6],16)) +
                           "_autorender_schematics"
                           ).resolve()
    if ofolder.exists():
        shutil.rmtree(ofolder)
    os.makedirs(ofolder)
    assert ofolder.exists()
    print("Tmp rendering folder:", ofolder)

    o = subprocess.run(kexport.render_schematic_wb_cmd(old_file, ofolder), stdout=subprocess.PIPE)
    old_out = o.stdout.decode('utf-8')
    n = subprocess.run(kexport.render_schematic_wb_cmd(new_file, ofolder), stdout=subprocess.PIPE)
    new_out = n.stdout.decode('utf-8')
    print("plotting schematics from kicad")
    print(old_out)
    print(new_out)
    print("plotting done")
    of = re.match(r"Plotted to \'(.*)\'", old_out, re.MULTILINE).group(1)
    nf = re.match(r"Plotted to \'(.*)\'", new_out, re.MULTILINE).group(1)

    print("diffing svg...")
    svg_diff_file = pathlib.Path(ofolder, "svgdiff.svg").resolve()
    kdiff_svg(of, nf, svg_diff_file)

    print('opening in web browser')
    webbrowser.open('file://' + os.path.realpath(svg_diff_file))
    exit()
