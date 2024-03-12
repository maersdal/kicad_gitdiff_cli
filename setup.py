from setuptools import setup

setup(
    name='kicad_gitdiff',
    version='0.0.5',
    url='https://github.com/maersdal/kicad_gitdiff_cli',
    license='Apache-2.0',
    license_files=["LICENSE"],
    author='magnus ersdal',
    author_email='magnus@resani.com',
    description='A tool for a visual diff with git and kicad',
    long_description="""
Simple visual diff for kicad 8 or higher. one can easily extend this tool to build a diff-er for anything that outputs svg.

This is not an official kicad tool or anything, just a friday night project.

My goal was just to get some `git` integration with the Kicad file formats.

[Documentation on github](https://github.com/maersdal/kicad_gitdiff_cli#readme)
""",
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=['git_config_template', 'kicad_export', 'sch_diff', 'svg_diff', 'checkers'],
    package_data={"git_config_template": ["*_template"]},
    include_package_data=True,
    entry_points={
        'console_scripts':
            ['kdiff_initialize = git_config_template:append_custom_git_config',
             'kicad_sch_diff = sch_diff:git_diff',
             ]
        },
    )
