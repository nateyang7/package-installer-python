# src/package_installer/package_installer.py

import platform
import os

class PackageInstaller:
    """
    Represents a package installer.

    Attributes:
        os (str): Operating system detected by the package installer.
        package_manager (str): Package manager from the operating system.
        packages (list[str]): Package's list.
    """

    __PROFILES_DIR: str = os.path.join("..", "..", "profiles")

    def __init__(self) -> None:
        """
        Initializes a package installer.
        """
        self.__os = platform.system()
        self.package_manager = self.get_package_manager()
        self.packages = self.get_packages()
        self.current_profile = "windows.txt"

    def get_package_manager(self) -> str:
        if self.__os == "Windows":
            return "winget"
        elif self.__os == "Linux":
            return "apt"  # Only support for Ubuntu / Debian (WILL SEE FOR OTHER DISTROS)
        elif self.__os == "Darwin":
            return "brew"
        else:
            return ''

    def get_packages(self) -> list[str]:
        """
        Returns packages from a file.

        Args:
            filepath (str): Path to the file.
        
        Returns:
            list[str]: Package's list from filepath.
        """
        if os.path.isdir(self.__PROFILES_DIR):
            filepath: str = os.path.join(self.__PROFILES_DIR, self.current_profile)
            print(filepath)
            with open(filepath, "r", encoding="utf-8") as f:
                return [package[:-1] for package in f.readlines()]

    def install_packages(self) -> None:
        ...
