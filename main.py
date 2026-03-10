# main.py

from src.package_installer import *

def main() -> int:
    packages: list[str] = get_json_packages("packages.json")
    install_packages(packages)
    
    return 0


main()
