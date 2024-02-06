#This Algorithm will translate a time expressed in seconds to a time expressed in days, hours, minutes and seconds.

TotalSeconds = input("Enter the number of seconds: ")

Timeafterdays = TotalSeconds % 86400
Days = (TotalSeconds - Timeafterdays)/86400

Timeafterhours = Timeafterdays % 3600
Hours = (Timeafterdays - Timeafterhours)/3600

Remainingseconds = Timeafterhours % 60
Minutes = (Timeafterhours - Remainingseconds)/60

print(f" {TotalSeconds} = {Days} days, {Hours} hours, {Minutes} minutes  ")






seconds = int(input("Enter the number of seconds: "))
mins= seconds/60
hours = seconds/3600
days = seconds/86400

#print(f"{seconds} seconds = {days} days, {hours} hours, {mins} minutes and {seconds} seconds.")
