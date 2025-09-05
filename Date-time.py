# datetime_operations.py
import request
from datetime import datetime, timedelta

# 1. Get current date and time
now = datetime.now()
print("🕒 Current Date and Time:", now)

# 2. Format date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("📅 Formatted Date and Time:", formatted)

# 3. Access specific parts
print("📆 Year:", now.year)
print("📆 Month:", now.month)
print("📆 Day:", now.day)
print("🕓 Hour:", now.hour)
print("🕔 Minute:", now.minute)
print("🕕 Second:", now.second)

# 4. Date arithmetic
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print("📅 Tomorrow:", tomorrow)
print("📅 Yesterday:", yesterday)

# 5. Custom date
custom_date = datetime(2025, 12, 25, 10, 30)
print("🎄 Custom Date:", custom_date)

# 6. Parse string to date
date_str = "2025-09-02 15:45:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("📜 Parsed Date from String:", parsed_date)
