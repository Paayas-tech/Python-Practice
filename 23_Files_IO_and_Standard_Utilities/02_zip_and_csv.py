import csv
import zipfile
from pathlib import Path

csv_filename = Path("team_data.csv")
zip_filename = Path("archive.zip")

# 1. Writing to a CSV file using csv.writer
headers = ["id", "name", "role", "city"]
rows = [
    [101, "Paayas", "Engineer", "Delhi"],
    [102, "Aarav", "Analyst", "Bengaluru"],
]

with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

# 2. Reading and iterating over CSV rows
with open(csv_filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print("CSV Header:", header_row)
    for record in reader:
        print("Record:", record)

# 3. Creating a Zip archive with zipfile
with zipfile.ZipFile(zip_filename, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    archive.write(csv_filename, arcname="team_data.csv")

# 4. Inspecting and reading from the Zip archive
with zipfile.ZipFile(zip_filename, "r") as archive:
    print("Files inside zip:", archive.namelist())
    info = archive.getinfo("team_data.csv")
    print(f"Uncompressed size: {info.file_size} bytes")

# Cleanup sample artifacts
if csv_filename.exists():
    csv_filename.unlink()
if zip_filename.exists():
    zip_filename.unlink()