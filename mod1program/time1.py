from datetime import datetime

#!print with year month date time
now = datetime.now()
print(now)

#!print current time
modified = now.strftime("%H:%M:%S")
print(modified)