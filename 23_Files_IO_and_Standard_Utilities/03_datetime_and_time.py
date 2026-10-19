import time
from datetime import datetime, timedelta

# 1. Working with current timestamp and formatted strings (strftime)
now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", formatted_now)

# 2. Parsing strings into datetime objects (strptime)
date_str = "2026-10-19 14:30:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed year:", parsed_date.year, "| Month:", parsed_date.month)

# 3. Date math using timedelta
tomorrow = now + timedelta(days=1)
thirty_minutes_ago = now - timedelta(minutes=30)
diff = tomorrow - now
print("Time delta in days:", diff.days)

# 4. Epoch timestamps and execution timing with the time module
start_time = time.time()
time.sleep(0.05)  # Sleep briefly
elapsed = time.time() - start_time
print(f"Elapsed time: {elapsed:.4f} seconds")