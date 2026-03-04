# src/package_installer/package_installer.py

import platform
import subprocess
from constants import *

def display_packages_status(packages: dict[str, str]) -> None:
    """
    Display status for each package contained in a dict.

    Args:
        packages (dict[str, str]): Dictionnary with packages and their status.
    
    Returns:
        None.
    """
    name_length: int = max(len(package_name) for package_name in packages.keys())

    print("=== PACKAGES ===")
    for package in packages:
        package_name: str = package + ' ' * (name_length - len(package))
        print(f"{package_name} => {packages[package]}")
    print()


def get_packages(filepath: str) -> list[str]:
    """
    Returns packages list from a file.

    Args:
        filepath (str): Path to the packages file.

    Returns:
        list[str]: List of packages contained at filepath.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return [package.strip() for package in f.readlines()]


def install_packages(packages: list[str]) -> None:
    """
    Install packages contained in a list.

    Args:
        packages (list[str]): Packages list.

    Returns:
        None.

    Examples:
        >>> install_packages(["Git.Git", "Python.Python3.10"])
    """
    packages_status: dict[str, str] = {package: '' for package in packages}

    print("INSTALLING PACKAGES...")
    if platform.system() == "Windows":
        for package in packages:
            installation: subprocess.CompletedProcess[bytes] = subprocess.run(
                [WINDOWS_PKGM, "install", "--id", package, "-e"],
                capture_output=True,
                text=True
            )
            if installation.stdout.strip().find(PACKAGE_INSTALLATION_SUCCESS) != -1:
                packages_status[package] = "Installed"
            elif PACKAGE_ALREADY_INSTALLED in installation.stdout.strip().split():
                packages_status[package] = "Already Installed"
            else:
                packages_status[package] = "Package not found"

    # LOGS
    display_packages_status(packages_status)


def remove_packages(packages: list[str]) -> None:
    """
    Remove packages from a list.

    Args:
        packages (list[str]): Packages list.

    Returns:
        None.
    """
    packages_status: dict[str, str] = {package: '' for package in packages}

    print("REMOVING PACKAGES...")
    if platform.system() == "Windows":
        for package in packages:
            removal: subprocess.CompletedProcess[bytes] = subprocess.run(
                [WINDOWS_PKGM, "uninstall", "--id", package],
                capture_output=True,
                text=True
            )

            if removal.stdout.strip().find(PACKAGE_REMOVAL_SUCCESS) != -1:
                packages_status[package] = "UNINSTALLED"
            else:
                packages_status[package] = removal.stderr

    display_packages_status(packages_status)


if __name__ == "__main__":
    # MUST FOLLOW -> [NOT_INSTALLED, INSTALLED, UNKNOWN]
    TEST_WINDOWS_PACKAGES: list[str] = ["Notepad++.Notepad++", "Git.Git", "pyton"]
    TEST_LINUX_PACKAGES: list[str] = ["gedit", "git", "pyton"]

    # WINDOWS: Ensure that you are on a windows machine before testing
    install_packages(TEST_WINDOWS_PACKAGES)
    remove_packages([TEST_WINDOWS_PACKAGES[0], ])

    print("All tests passed!")
