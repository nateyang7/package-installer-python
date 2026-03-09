# main.py

from src.package_installer import *

def main() -> int:
    packages: list[str] = get_packages("packages.txt")
    install_packages(packages)
    
    return 0


main()
