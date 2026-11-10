import sys
import os

try:
    from pathlib import Path
    from rich.console import Console


    con: Console = Console()
except ImportError as Error:
    sys.exit(
        f"\x1b[31merror:\x1b[0m {Error}"
    )

class App:
    def __init__(self) -> None:
        if os.name == "nt":
            import winreg

            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
        else:
            downloads_dir = Path.home() / "Downloads"
    
        self.downloads_dir: str = Path.home / "Downloads"
