# main.py

from package_installer.package_installer import *
from package_installer.package_manager import *

def main() -> int:
    packages: list[str] = get_packages("packages.txt")
    install_packages(packages)
    
    return 0


main()
