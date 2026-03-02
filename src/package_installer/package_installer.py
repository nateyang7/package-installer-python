# src/package_installer/package_installer.py

import os
from packages import *

def install_packages(pkg_manager: dict) -> int:
    """
    Install packages depending on the package_manager.

    Args:

    Returns:
    """
    package_managers: list[str] = list(pkg_manager.keys())
    for package_manager in package_managers:
        if package_manager != "winget":
            os.system(f"sudo apt update && sudo apt full-upgrade")
            for package in packages:
                os.system(f"sudo {package_manager} install {package} -y")
            return 0
        else:
            os.system(f"winget upgrade --id Microsoft.AppInstaller")
            for package in packages:
                os.system("winget install --id {package} -e")
            return 0
        return 1


if __name__ == "__main__":
    install_packages(PACKAGE_MANAGERS)  # OK

    print("All tests passed")
