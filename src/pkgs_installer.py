"""
"""

import os
import platform

class Pkgs_Installer:
    """
    Represents a package installer.

    Attributes:
        __WINDOWS_PMS (str): Constant for the official pms on Windows.
        __MACOS_PMS (str): Constant for the official pms on MacOS.
        __pms (str): Package Management System detected.
    """
    __WINDOWS_PMS: str = "winget"
    __MACOS_PMS: str = "brew"

    def __init__(self) -> None:
        """
        Initializes a package installer.
        """
        self.__pms = self.detect_pms()

    @property
    def pms(self) -> str:
        """ Getter of the package management system. """
        return self.__pms

    def detect_pms(self) -> str:
        """
        Returns the package management system depending on the OS.

        Returns:
            str: PMS detected on the system.
        """
        if platorm.system() == "Windows":
            return self.__WINDOWS_PMS
        elif platform.system() == "Darwing":
            return self.__MACOS_PMS
        elif platform.system() == "Linux":
            try:
                with open("/etc/os-release") as f:
                    info: str = f.read()
                    if "ubuntu" in info.lower() or "debian" in info.lower():
                        return "apt"
                    elif "fedora" in info.lower() or "red hat" in info.lower():
                        return "dnf"
                    elif "arch" in info.lower():
                        return "pacman"
                    else:
                        return "unknown"
            except FileNotFoundError:
                return "unknown"
        else:
            return "unknown"

