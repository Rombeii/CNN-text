import pandas as pd
from pathlib import Path


data_folder = Path("Resources/bbc")

text = []
label = []

for folder_path in data_folder.iterdir():
    if folder_path.is_dir():
        folder_name = folder_path.name
        files = folder_path.glob("*.txt")
        for file_path in files:
            with file_path.open() as file:
                data = file.read()
            text.append(data)
            label.append(folder_name)

data = {'news': text, 'type': label}
df = pd.DataFrame(data)
df.to_csv('Resources/bbc.csv', index=False)
