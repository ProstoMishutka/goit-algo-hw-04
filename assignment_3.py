from colorama import Fore, Style
from pathlib import Path
import sys

def way_folder():
    if len(sys.argv) < 2:
        way = ""
    else:
        way = sys.argv[1]
    path = Path(way)
    if path.exists():
        if path.is_dir():
            for el in path.iterdir():
                if el.is_file():
                    print(f"{Fore.YELLOW}{el.name}{Style.RESET_ALL}")
                elif el.is_dir():
                    print(f"{Fore.BLUE}{el.name}{Style.RESET_ALL}")
        else:
            print(f"{way} is not a directory.")
    else:
        print(f"{way} does not exist.")

way_folder()