import platform
import shutil
import subprocess

class LazyPkg:
    """
    Represents an app for automated installation of packages.

    Attributes:
        platform (str): OS Name.
        pkg_manager (str): Package manager.
        pkgs (list[str]): Packages to install from a data file. 
    """

    def __init__(self) -> None:
        """
        Initializes an object of the installation app.
        """
        self.platform = platform.system()
        self.pkg_manager = ...
        self.pkgs = ...

    def get_pkg_manager(self) -> str:
        ...

    def install_pkgs(self) -> None:
        """ Install packages from a data file """
        ...

