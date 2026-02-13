years = (int(input("Enter number of year/s: ")))
converter = years*365*24*60*60
# 365 days in 1 year 24 hours in 1 day 60 minutes in 1 hour 60 seconds in 1 minute
print(f"{years} years in seconds is {converter}.")