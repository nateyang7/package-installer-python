# tests/test_package_installer.py

import pytest
import platform
from src.package_installer.package_installer import PackageInstaller

@pytest.fixture
def package_installer() -> PackageInstaller:
    return PackageInstaller()


def test_get_package_manager(package_installer: PackageInstaller) -> None:
    if platform.system() == "Windows":
        assert package_installer.get_package_manager() == "winget"
    elif platform.system() == "Linux":
        assert package_installer.get_package_manager() == "apt"
    elif platform.system() == "Darwin":
        assert package_installer.get_package_manager() == "brew"


def test_get_packages(package_installer: PackageInstaller) -> None:
    if platform.system() == "Windows":
        assert package_installer.get_packages() == ["Git.Git", "Neovim.Neovim", "Python.Python.3.10"]
