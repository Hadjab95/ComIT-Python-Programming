#This Algorithm will translate a time expressed in seconds to a time expressed in days, hours, minutes and seconds.
seconds = int(input("Enter the number of seconds: "))
mins= seconds/60
hours = seconds/3600
days = seconds/86400

print(f"{seconds} seconds equals: {days} days, {hours} hours, {mins} minutes and {seconds}.")