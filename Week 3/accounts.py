'''
accounts.py

The objective of this program is to read a 10 character account number and output the account number
with only the last 4 digits showing. 
Update - It's been updated to prevent the user from using letters and non digits.

Author: Loic Bagnoud
'''

# I came back to this to add a condition for strings and letters to prevent the user from going ahead and adding things that don't belong.
# This was achieved with a nifty function called "check_for_string".

# As we can see from this function, we have a while loop that asks the user for the input, same as my original version, and stores it
# in a variable called account. 

def check_for_string():
    while True:
        account = input("Please enter an account number ")

# Then, we just create a simple if statement checking if that variable is a digit with the .isdigit function. If it isn't,
# we print that statement asking the user to please user numbers and not letters. We then use the continue function to proceed (we don't really need an else statement)
# and we return the account. 

        if not account.isdigit():
            print("Please make sure you are only using numbers. Letters are not allowed!")
            continue
        
        return account

# We go ahead and store that function into the variable called account_number which we'll be using from now on.
account_number = check_for_string()


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

# Finally, we just print the encrypted_account_number that was defined in the variable above. Currently this program only works with account numbers of any size
print(f"Your encrypted account number is: {encrypted_account_number}") 



# References: 

# Stack overflow discussion on hiding all but the last 4 digits: #https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python

# Concatenate and slicing strings: https://www.w3schools.com/python/python_strings_slicing.asp and https://www.w3schools.com/python/python_strings_concatenate.asp

# While loop and Continue function: https://www.w3schools.com/python/python_while_loops.asp
#                                   https://www.w3schools.com/python/ref_keyword_continue.asp

# isdigit function - https://www.w3schools.com/python/ref_string_isdigit.asp

# Chatgpt for help with correcting my erroneous syntax - I forgot to save my prompt or his response but as explained, he merely stated that .replace was too cumbersome. And that
# it could be simplified by the solution above. I understood his solution and it was a bit more elegant than what I found.