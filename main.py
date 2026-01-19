"""
TO-DO:
    - [] 
"""
import os, platform, subprocess

PACKAGES: dict[str, list[str]] = {
        "Windows": ["Vim.Vim", "Git.Git", "Mozilla.Firefox"],
        "Linux": ["vim", "git", "firefox"],
}

def install_packages() -> int:
    """
    Install packages depending on the operation system.

    Returns:
        int: 0 if no problems else 1.
    """
    global PACKAGES
    if platform.system() == "Windows":
        return 0
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "apt", "update", "&&", "full-upgrade", "-y"])
        for package in PACKAGES[platform.system()]:
            subprocess.run(["sudo", "apt", "install", package])
        return 0
    else:
        return 1

def main() -> int:
    install_packages()
    return 0


main()
