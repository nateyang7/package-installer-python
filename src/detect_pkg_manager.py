#!/usr/bin/env python3
from typing import Callable
import platform
import shutil

def detect_pkg_manager() -> str:
    """
    Get the package manager from the user's OS.

    Returns:
        str: Package manager name depending on the user's OS.
    """
    PKG_MANAGERS: dict[str, str] = {
            "Darwin": "brew",  # MacOS
            "Windows": "winget",  # Windows
            "Linux": "apt"  # Linux (REVOIR SI AJOUT D'AUTRES DISTROS)
            }
    system: str = platform.system()
    return PKG_MANAGERS[system]


if __name__ == "__main__":
    TEST_SYSTEM: str = platform.system()

    print(TEST_SYSTEM)

    if TEST_SYSTEM == "Darwin":
        assert detect_pkg_manager() == "brew"
    if TEST_SYSTEM == "Windows":
        assert detect_pkg_manager() == "winget"
    if TEST_SYSTEM == "Linux":
        assert detect_pkg_manager() == "apt"

    print("All tests passed!")

