import os
from pathlib import Path

# 1. Directory and Path handling using modern pathlib
base_dir = Path("sample_folder")
base_dir.mkdir(exist_ok=True)

file_path = base_dir / "sample.txt"

# 2. Writing and Reading with the 'with' context manager
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Line 1: Practical Python file operations\n")
    f.write("Line 2: Context managers automatically handle closing\n")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print("File Content:\n", content)

# 3. Path inspection and iterating directories
print(f"File exists: {file_path.exists()}")
print(f"File name: {file_path.name}")
print(f"File suffix: {file_path.suffix}")

for item in base_dir.iterdir():
    print("Found item in folder:", item.name)

# 4. Cleanup using pathlib's unlink() and os.rmdir()
if file_path.exists():
    file_path.unlink()  # Removes the file
base_dir.rmdir()       # Removes the empty directory