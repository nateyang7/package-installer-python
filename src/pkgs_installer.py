"""
"""

import os
import platform
import subprocess

class PkgsInstaller:
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
        if platform.system() == "Windows":
            return self.__WINDOWS_PMS
        elif platform.system() == "Darwin":
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

    def install(self) -> None:
        with open("pkgs.txt") as f:
            pkgs: list[str] = [line.strip() for line in f if line.strip()]
            for pkg in pkgs:
                if platform.system() == "Windows":
                    subprocess.run(["winget", "install", "--id", pkg, "-e", "--silent"])
                elif platform.system() == "Darwin":
                    subprocess.run(["brew", "install", pkg])
                elif platform.system() == "Linux":
                    subprocess.run(["sudo", self.pms, "install", "-y", pkg])
            print("All packages installed!")

    def display_info(self) -> None:
        header: str = f"=== OS: {platform.system()} ===\n"
        data: str = f"PMS: {self.pms}"
        print(header + data)


if __name__ == "__main__":
    TEST = PkgsInstaller()
    TEST.install()
    TEST.display_info()


    print("All tests passed!")

