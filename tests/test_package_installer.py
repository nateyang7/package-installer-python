# tests/test_package_installer.py

import pytest
from os.path import join
from package_installer.package_installer import *

TEST_PACKAGES_FILE: str = join("tests", "windows_packages_test.txt")

def test_get_packages() -> None:

    assert get_packages(TEST_PACKAGES_FILE) == ["Notepad++.Notepad++", "Git.Git", "python"]
