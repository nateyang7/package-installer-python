# src/package_installer/package_installer.py

import platform
import subprocess
import json

# === Constants & Enums ===
INSTALLATION_ERROR: int = 0
PACKAGE_INSTALLATION_SUCCESS: str = 'Successfully installed'
PACKAGE_ALREADY_INSTALLED: str = 'Found'
PACKAGE_REMOVAL_SUCCESS: str = 'Successfully uninstalled'

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

    print('\n=== PACKAGES ===')
    for package in packages:
        package_name: str = package + ' ' * (name_length - len(package))
        print(f'{package_name} => {packages[package]}')
    print()


def get_json_packages(filepath: str) -> list[str]:
    """
    Returns packages list from a JSON file.

    Args:
        filepath (str): Path to JSON file.

    Returns:
        list[str]: List of packages contained at filepath.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        packages: dict[str, list[str]] = json.load(f)
        return packages[platform.system()]


def get_linux_package_manager() -> str:
    """
    Returns package manager on a Linux distribution.

    Returns:
        str: Package manager from the current Linux distribution.
    """
    with open('/etc/os-release', 'r') as f:
        info: str = f.read().lower()

    if 'ubuntu' in info or 'debian' in info:
        return 'apt'
    elif 'fedora' in info or 'centos' in info or 'rhel' in info:
        return 'dnf'
    elif 'arch' in info:
        return 'pacman'


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

    print('INSTALLING PACKAGES...')
    if platform.system() == 'Windows':
        for package in packages:
            installation: subprocess.CompletedProcess[bytes] = subprocess.run(
                ['winget', 'install', '--id', package, '-e'],
                capture_output=True,
                text=True
            )

            if installation.stdout.strip().find(PACKAGE_INSTALLATION_SUCCESS) != -1:
                packages_status[package] = 'Installed'
            elif PACKAGE_ALREADY_INSTALLED in installation.stdout.strip().split():
                packages_status[package] = 'Already Installed'
            else:
                packages_status[package] = 'Package not found'

    elif platform.system() == 'Linux':
        package_manager = get_linux_package_manager()
        for package in packages:
            installation: subprocess.CompletedProcess[bytes] = subprocess.run(
                ['sudo', package_manager, 'install', package],
                text=True
            )

            if installation.returncode == 0:
                packages_status[package] = 'Installed / Already Installed'
            else:
                packages_status[package] = 'Package not found'

    
    elif platform.system() == 'Darwin':
        for package in packages:
            installation: subprocess.CompletedProcess[bytes] = subprocess.run(
                ['brew', 'install', package],
                capture_output=True,
                text=True
            )

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

    print('REMOVING PACKAGES...')
    if platform.system() == 'Windows':
        for package in packages:
            removal: subprocess.CompletedProcess[bytes] = subprocess.run(
                [PackageManager.WINDOWS, 'uninstall', '--id', package],
                capture_output=True,
                text=True
            )

            if removal.stdout.strip().find(PACKAGE_REMOVAL_SUCCESS) != -1:
                packages_status[package] = 'UNINSTALLED'
            else:
                packages_status[package] = removal.stderr

    display_packages_status(packages_status)

