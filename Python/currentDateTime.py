# Display current date and time

import datetime

now = datetime.datetime.now()
print(f'Current Date & Time:', now.strftime("%Y-%m-%d %H:%M:%S"))