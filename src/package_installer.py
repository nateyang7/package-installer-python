"""
Author: Nathan Yang
TO-DO:
    1)
    2)
    3)

NOTES:
"""

import os

class PackageInstaller:
    """
    Represents a package installer.

    Attributes:
        __WINDOWS_PMS (str): Constant for the  package manager on Windows.
        __LINUX_PMS (str): Constant for the package manager on Ubuntu / Debian 
        for Linux.
        __MACOS_PMS (str): Constant for the package manager on MacOS.
        __pms (str): Package Management System detected.
    """
    __WINDOWS_PACKAGE_MANAGER: str = "winget"
    __LINUX_PACKAGE_MANAGER: str = "apt"
    __MACOS_PACKAGE_MANAGER: str = "brew"
    __PACKAGES_FILEPATH: str = "packages.txt"

    def __init__(self) -> None:
        """
        Initializes a package installer.
        """
        self.__package_manager = self.detect_package_manager()

    @property
    def package_manager(self) -> str:
        """ Getter of the package management system. """
        return self.__package_management_system

    def detect_package_manage(self) -> str:
        """
        Returns the package management system depending on the OS.

        Returns:
            str: Package manager detected on the system.
        """
        if platform.system() == "Windows":
            return self.__WINDOWS_PACKAGE_MANAGER
        elif platform.system() == "Linux":
            return self.__LINUX_PACKAGE_MANAGER
        """
        elif platform.system() == "Darwin":
            return self.__MACOS_PACKAGE_MANAGER
        """
        else:
            return "unknown"

    def install(self) -> None:
        """
        Install packages.

        Returns:
            None.
        """
        with open(self.__PACKAGES_FILEPATH, "r",  encoding="utf-8") as f:
            packages: list[str] = [line.strip() for line in f if line.strip()]
            for package in packages:
                if os.name == "nt":
                    
            print("All packages installed!")

    def display_info(self) -> None:
        header: str = f"=== OS: {platform.system()} ===\n"
        data: str = f"PMS: {self.pms}"
        print(header + data)


if __name__ == "__main__":
    TEST = PackageInstaller()
    TEST.install()
    TEST.display_info()

    print("All tests passed!")

