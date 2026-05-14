# hello.py

# Python script: user types their name 
# → script prints a welcome message, today's date,
#  and day of week. 
# Run it from terminal. Push to GitHub with a README.
from datetime import date

name = input("Name?")
print(f"Hello {name} and today date is:  {date.today()}")
 
