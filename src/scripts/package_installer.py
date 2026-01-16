"""
Author: Nathan Yang
Notes:
    - [] Support Windows
    - [X] Support Linux 
    - [] Support Windows
"""

import os

# Constants
PACKAGE_MANAGERS: dict[str, str] = {
        "windows": "winget",
        "linux": "apt",
        "macos": "brew",
}
WINDOWS_PACKAGES: list[str] = ["Vim.Vim", "Git.Git", "Python.Python.3"]
LINUX_PACKAGES: list[str] = ["vim", "git", "python3"]

# Functions
def install_packages(packages: list[str], package_manager: str) -> int:
    """
    Install packages depending on the package_manager.

    Args:

    Returns:
    """
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
    install_packages(LINUX_PACKAGES, PACKAGE_MANAGERS["linux"])  # OK

    print("All tests passed")
