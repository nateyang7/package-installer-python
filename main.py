# main.py

from src.package_installer import get_json_packages, install_packages

def main() -> int:
    packages: list[str] = get_json_packages("packages.json")
    install_packages(packages)
    
    return 0


if __name__ == "__main__":
    main()
