# src/package_installer/package_manager.py

from enum import StrEnum

class PackageManager(StrEnum):
    WINDOWS = "winget"
    LINUX = "apt"
    MACOS = "brew"
