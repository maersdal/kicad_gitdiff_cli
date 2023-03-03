import glob
import subprocess
import pathlib
import re
import os


def get_kicad_cli():
    return r"kicad-cli"


def get_export_cmd():
    return "sch export svg --black-and-white"


def output_cmd(ofolder):
    return f"--output {ofolder}"


def sch_files(folder):
    return glob.glob(f"{folder}/*.kicad_sch")


def create_render_folder(folder):
    render_path = pathlib.Path(folder).resolve()
    if not os.path.exists(render_path):
        print("creating output folder ", render_path)
        os.makedirs(render_path)

def render_schematic_wb_cmd(file, ofolder):
    return f"{get_kicad_cli()} {get_export_cmd()} {output_cmd(ofolder)} {file}"

def render_schematics_from_folder(folder, ofolder) -> list[str]:
    create_render_folder(ofolder)
    return [render_schematic_wb_cmd(f, ofolder) for f in sch_files(folder)]