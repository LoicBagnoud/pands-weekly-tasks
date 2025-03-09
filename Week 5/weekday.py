'''
weekday.py

The objective of this program is to find out whether it's weekday or not and output its result.

Author: Loic Bagnoud
'''

# This was not as hard as I thought. I found out about the datetime package and basically imported it as shown.
import datetime

# Created a variable called today in referece to the day this program is run and then found out how to search and see what current day of the week it is
# with the datetime package.
today = datetime.date.today()

# Afterwards, created a simple if else statement that prints accordingly, depending if the today is less than 5 (seeing as the weekdays in the package are numbered 
# 0 to 4), then it should print that it is a weekday.
if today.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")


# References:

# Datetime package and weekday references - https://docs.python.org/3/library/datetime.html

# Confirmed with Chatgpt how we can actually check the system date and time
# Prompt: The statement datetime.date.today() is what allows us to check for the current date? How does that work?

# Chatgpt answer: datetime.date.today() is a method from Python's built-in datetime module. 
#                 It returns a date object representing today's date according to your system's local date. 
#                 This object includes the year, month, and day, which you can then use for further date manipulations or comparisons.