# tests/test_package_installer.py

import pytest
from os.path import join
from package_installer.package_installer import *

TEST_PACKAGES_FILE: str = join("tests", "windows_packages_test.txt")
TEST_WINDOWS_PACKAGES: list[str] = ["Notepad++.Notepad++", "Git.Git", "pyton"]
TEST_LINUX_PACKAGES: list[str] = ["gedit", "git", "pyton"]

def test_get_packages() -> None:
    assert get_packages(TEST_PACKAGES_FILE) == ["Notepad++.Notepad++", "Git.Git", "python"]


def test_package_installer() -> None:
    successful_tests: int = 0

    install_packages(TEST_WINDOWS_PACKAGES)
    successful_tests += 1
    remove_packages([TEST_WINDOWS_PACKAGES[0], ])
    successful_tests += 1

    assert successful_tests == 2
