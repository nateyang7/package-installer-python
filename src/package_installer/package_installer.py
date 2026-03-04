# src/package_installer/package_installer.py

import platform
import subprocess

INSTALLATION_ERROR: int = 0
PACKAGE_INSTALLATION_SUCCESS: str = "Successfully installed"
PACKAGE_ALREADY_INSTALLED: str = "Found"

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
    installed_packages: dict[str, str] = {package: '' for package in packages}

    if platform.system() == "Windows":
        for package in packages:
            installation: subprocess.CompletedProcess[bytes] = subprocess.run(
                ["winget", "install", "--id", package, "-e"],
                capture_output=True,
                text=True
            )
            if installation.stdout.strip().find(PACKAGE_INSTALLATION_SUCCESS):
                installed_packages[package] = "Installed"
            elif PACKAGE_ALREADY_INSTALLED in installation.stdout.strip().split():
                installed_packages[package] = "Already Installed"
            else:
                installed_packages[package] = "Package not found"

    # LOGS
    display_packages_status(installed_packages)


def remove_packages(packages: list[str]) -> None:
    """
    Remove packages from a list.

    Args:
        packages (list[str]): Packages list.

    Returns:
        None.
    """
    ...


if __name__ == "__main__":
    # Ensure that git is installed before testing
    test_windows_packages: list[str] = ["Notepad++.Notepad++", "Git.Git", "python"]

    #remove_packages()
    install_packages(test_windows_packages)

    print("All tests passed!")
