# src/package_installer/package_installer.py

import platform
import subprocess

INSTALLATION_ERROR: int = 0
PACKAGE_INSTALLATION_SUCCESS: str = ""
PACKAGE_ALREADY_INSTALLED: str = "Found"
ERROR_PACKAGE_NOT_FOUND: str = "No package found matching input criteria."

def display_packages_status(packages: dict) -> None:
    """
    Display status for each package contained in a dict.

    Args:
        packages (dict): Packages dict.
    
    Returns:
        None.
    """
    name_length: int = max(len(package_name) for package_name in packages.keys())

    print("=== PACKAGES ===")
    for package in packages:
        if len(package) == name_length:
            print(f"{package} => {packages[package]}")
        else:
            print(f"{package + ' ' * (name_length - len(package))} => {packages[package]}")


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
            if PACKAGE_INSTALLATION_SUCCESS in installation.stdout.strip().split():
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
    test_success_packages: list[str] = ["Git.Git", "Mozilla.Firefox", "potato"]
    #test_error_packages: list[str] = ["apple", "potato", "banana"]

    install_packages(test_success_packages)
    #install_packages(test_error_packages)  # => Verify return code

    print("All tests passed!")
