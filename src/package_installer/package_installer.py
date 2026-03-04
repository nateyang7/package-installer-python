# src/package_installer/package_installer.py

import platform
import subprocess

INSTALLATION_ERROR: int = 0
ERROR_PACKAGE_NOT_FOUND: str = "No package found matching input criteria."

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
    installed_packages: dict[str, str] = {package: '?' for package in packages}

    if platform.system() == "Windows":
        for package in packages:
            installation: subprocess.CompletedProcess[bytes] = subprocess.run(
                ["winget", "install", "--id", package, "-e"],
                capture_output=True,
                text=True
            )
            if installation.returncode != INSTALLATION_ERROR:
                installed_packages[package] = "Installed"
            else:
                installed_packages[package] = installation.returncode

    # LOGS
    print("=== PACKAGES ===")
    for package in installed_packages:
        print(f"{package}: {installed_packages[package]}")
    print()


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
    test_error_packages: list[str] = ["apple", "potato", "banana"]

    install_packages(test_success_packages)
    install_packages(test_error_packages)

    print("All tests passed!")
