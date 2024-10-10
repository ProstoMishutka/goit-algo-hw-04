from pathlib import Path
from colorama import Fore, Style

def way_folder(path, n=1):
    path = Path(path)
    space = " " * (n * 4)
    if path.exists():
        for element in path.iterdir():
            if element.is_file():
                print(f"{space}{Fore.YELLOW}{element.name}{Style.RESET_ALL}")
            else:
                print(f"{space}{Fore.BLUE}{element.name}{Style.RESET_ALL}")
                way_folder(element, n + 1)

path = "."
way_folder(path)
