#This will translate a time expressed in days, hours, minutes and seconds into time expressed in seconds

days = float(input("Enter the # of days: "))
hours =  float(input("Enter the # of hours: ")) 
minutes = float(input("Enter the # of minutes: "))
seconds = float(input("Enter the # of seconds: "))

print(f"You entered {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")
total_in_seconds = days*86400 + hours*3600 + minutes*60 + seconds

print(f"That's {total_in_seconds} seconds")

