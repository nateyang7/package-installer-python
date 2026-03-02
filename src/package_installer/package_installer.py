# src/package_installer/package_installer.py

import platform

class PackageInstaller:
    """
    Represents a package installer.

    Attributes:
        os (str): Operating system detected by the package installer.
        package_manager (str): Package manager from the operating system.
    """

    def __init__(self) -> None:
        """
        Initializes a package installer.
        """
        self.os = platform.system()
        self.package_manager = self.get_package_manager()
        self.packages_filepath = self.get_packages_filepath()

    def get_package_manager(self) -> str:
        if self.os == "Windows":
            return "winget"
        elif self.os == "Linux":
            return "apt"  # Only support for Ubuntu / Debian (WILL SEE FOR OTHER DISTROS)
        elif self.os == "Darwin":
            return "brew"
        else:
            ...

    def get_packages_filepath(self) -> str:
        ...

    def install_packages(self) -> None:
        ...