from pathlib import Path

folder = Path("sandbox")
for item in folder.iterdir():
    if item.is_file():
        print(item.name, "->", item.suffix)