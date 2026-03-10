# tests/test_package_installer.py

import pytest
from os.path import join
from platform import system
from package_installer import *

TEST_PACKAGES_FILE: str = join("tests", "packages_test.json")
TEST_WINDOWS_PACKAGES: list[str] = ["Notepad++.Notepad++", "Git.Git", "pyton"]
TEST_UNIX_PACKAGES: list[str] = ["notepad-plus-plus", "git", "pyton"]

def test_get_json_packages() -> None:
    if system() == "Windows":
        assert get_json_packages(TEST_PACKAGES_FILE) == TEST_WINDOWS_PACKAGES
    elif system() == "Linux" or system == "Darwin":
        assert get_json_packages(TEST_PACKAGES_FILE) == TEST_UNIX_PACKAGES


def test_package_installer() -> None:
    successful_tests: int = 0

    if system() == "Windows":
        install_packages(TEST_WINDOWS_PACKAGES)
        successful_tests += 1
        remove_packages([TEST_WINDOWS_PACKAGES[0], ])
        successful_tests += 1

    elif system() == "Linux":
        install_packages(TEST_UNIX_PACKAGES)
        successful_tests += 1
        remove_packages([TEST_UNIX_PACKAGES[0], ])
        successful_tests += 1

    elif system == "Darwin":
        install_packages(TEST_UNIX_PACKAGES)
        successful_tests += 1
        remove_packages([TEST_UNIX_PACKAGES[0], ])
        successful_tests += 1

    assert successful_tests == 2
