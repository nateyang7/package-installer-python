# src/package_installer/package_installer.py

import platform
import subprocess
from enum import StrEnum

# === Constants & Enums ===
class PackageManager(StrEnum):
    WINDOWS = "winget"
    LINUX = "apt"
    MACOS = "brew"

INSTALLATION_ERROR: int = 0
PACKAGE_INSTALLATION_SUCCESS: str = "Successfully installed"
PACKAGE_ALREADY_INSTALLED: str = "Found"
PACKAGE_REMOVAL_SUCCESS: str = "Successfully uninstalled"


# === Functions ===
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
                [PackageManager.WINDOWS, "install", "--id", package, "-e"],
                capture_output=True,
                text=True
            )
            if installation.stdout.strip().find(PACKAGE_INSTALLATION_SUCCESS) != -1:
                packages_status[package] = "Installed"
            elif PACKAGE_ALREADY_INSTALLED in installation.stdout.strip().split():
                packages_status[package] = "Already Installed"
            else:
                packages_status[package] = "Package not found"

    elif platform.system() == "Linux":
        ...
    
    elif platform.system() == "Darwin":
        ...

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
                [PackageManager.WINDOWS, "uninstall", "--id", package],
                capture_output=True,
                text=True
            )

            if removal.stdout.strip().find(PACKAGE_REMOVAL_SUCCESS) != -1:
                packages_status[package] = "UNINSTALLED"
            else:
                packages_status[package] = removal.stderr

    display_packages_status(packages_status)


if __name__ == "__main__":
    install_packages(["Neovim.Neovim", "WiresharkFoundation.Wireshark"])

    print("All tests passed!")
