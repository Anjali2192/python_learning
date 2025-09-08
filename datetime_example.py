from datetime import datetime

now = datetime.now()

print("Today's Date:", now.date())
print("Today's Time:", now.time())

print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))