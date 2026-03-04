# src/package_installer/constants.py

# Package managers
WINDOWS_PKGM: str = "winget"
LINUX_PKGM: str = "apt"  # Check support for Fedora and Arch later
MACOS_PKGM: str = "brew"

# Installation / Removal status
INSTALLATION_ERROR: int = 0
PACKAGE_INSTALLATION_SUCCESS: str = "Successfully installed"
PACKAGE_ALREADY_INSTALLED: str = "Found"
PACKAGE_REMOVAL_SUCCESS: str = "Successfully uninstalled"
