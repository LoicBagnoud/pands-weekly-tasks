'''
accounts.py

The objective of this program is to read a 10 character account number and output the account number
with only the last 4 digits showing.

Author: Loic Bagnoud
'''

# This was a very tricky one honestly... And I had to refer to chatgpt for a correction but let's go for it.
# This first part was just getting the input which was easy.

account_number = (input("Please enter an account number "))

# The issue came here. I found a stack overflow discussion which provided some insights. 
# Eventually, this was my attempted code:
'''
account_number_length = len(account_number)
encrypted_account_number = account_number.replace(account_number_length([0:-4]"X"))
'''
# Didn't work. Got an Invalid Syntax error that I asked ChatGPT about and then he corrected my syntax and stated that .replace was not needed. I ended up with this:
encrypted_account_number = "X" * (len(account_number) - 4) + account_number[-4:]

# As we can see and my understanding of this is that we have X (the string), multiplied by the length (the length is variable and can be any amount) minus 4 to match the 
# fact that the last 4 digits must be preserved and not encrypted.
# We then concatenate with the account number that was inputted but only the last 4 digits, starting from the end until the fourth.
# I imagine that if we want the user to only use 10 digits, we would need an If statement...  

# Finally, we just print the encrypted_account_number that was defined in the variable above.
print(f"Your encrypted account number is: {encrypted_account_number}") 



# Currently this program only works with account numbers of any size 
# I imagine that if we want the user to only use 10 digits, we would need an If statement... Something along of the lines
# of If account_number is >10 then print("Please make sure you're imputting a 10 numbered account") or something like this

# References: 

# Stack overflow discussion on hiding all but the last 4 digits: #https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python

# Concatenate and slicing strings: https://www.w3schools.com/python/python_strings_slicing.asp and https://www.w3schools.com/python/python_strings_concatenate.asp

# Chatgpt for help with correcting my erroneous syntax
