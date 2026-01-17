WINDOWS_PACKAGES: list[str] = ["Vim.Vim", "Git.Git", "Python.Python.3"]
LINUX_PACKAGES: list[str] = ["vim", "git", "python3"]
MACOS_PACKAGES: list[str] = []

PACKAGE_MANAGERS: dict[str, str] = {
        "winget": WINDOWS_PACKAGES,
        "apt":  LINUX_PACKAGES,
        "brew": MACOS_PACKAGES,
}

