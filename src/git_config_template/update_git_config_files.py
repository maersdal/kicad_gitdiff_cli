import pathlib
DEBUGPATH = False
git_test_folder = ".\\git_test_folder"
is_test = pathlib.Path(git_test_folder).exists()


def is_git_repo():
    return pathlib.Path(".\\.git").exists() or is_test


gitconfig_template = pathlib.Path(pathlib.Path(__file__).parent, pathlib.Path("gitconfig_template")).open('r').read()
gitattributes_template = pathlib.Path(pathlib.Path(__file__).parent, pathlib.Path("gitattributes_template")).open(
    'r').read()


def append_custom_git_config():
    if DEBUGPATH:
        print(gitattributes_template)
        print(gitconfig_template)
    gitfolder = ".\\.git"
    if is_test:
        gitfolder = git_test_folder
    if DEBUGPATH:
        gfp = pathlib.Path(gitfolder).resolve()
        print(gfp, gfp.exists())
        print(__file__)

    x = input("Warning: will modify your git repository settings, needs only to be done once. \n is this ok? ([y]/n)")
    if (x == "") or (x.lower() == 'y'):
        pass
    else:
        exit()
    if is_git_repo():
        pass
    else:
        print("not in a git repo... exiting")
        exit()

    with open(gitfolder + "\\config", 'a') as f:
        f.write(gitconfig_template)

    with open(".gitattributes", 'a') as f:
        f.write(gitattributes_template)


if __name__ == '__main__':
    append_custom_git_config()
