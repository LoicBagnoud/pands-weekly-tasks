'''
bank.py

The objective of this program is to prompt the user to input two ammounts in cents and sum up the results, 
printing out the result in a human readable format with a euro sign and decimal point between the euro and cent of the amount

author: Loic Bagnoud
'''

# I went back to this and tried to understand how I could prevent a user from using commas or dots. I used chatgpt to help me with this.

# Because of the differences between strings and integers and the fact that a comma and a dot is treated as a string, I first asked the user
# to input things as a string. In other words, whatever the user puts (in numbers) will be a string. So that we can recognise the commas and the dots. 
# I called it ammount_str for both the first and second try.
# I also had to use a While loop to force the user to input a proper value so the code does not move from this until the user inputs correctly.
while True:
    amount1_str = input('Enter the first amount (in cent): ')

# Then, I used an if statement to find specific strings in whatever they put. If it finds it, it prints out a message to correct the value.
    if '.' in amount1_str or ',' in amount1_str:
        print("Please enter the amount in cents without dots or commas!")

# If everything is put correctly, we can then convert the string the user put into an actual integer.
    else:
        amount1 = int(amount1_str)
        break
    
# This one follows the same logic as the one above.
while True:
    amount2_str = input('Enter the second amount (in cent): ')
    if '.' in amount2_str or ',' in amount2_str:
        print("Please enter the amount in cents without dots or commas!")
    else:
        amount2 = int(amount2_str)
        break


# I went ahead and summed up the ammounts, dividing them by 100. I made sure to use brackets so that the division goes first
result = (amount1/100) + (amount2/100)


# I struggled with this but I took it in parts. I tried to first assign a variable called txt and formatted the string to display the result (2 decimal points up) and 
# then researched how I could present the euro sign. References at the bottom.

txt = f"The sum of these is {result:.2f}%s"%u"\N{euro sign}"

# Finally, I just printed the above.
print(txt)

# References:

# For the {result:.2f} part - https://www.w3schools.com/python/python_string_formatting.asp#gsc.tab=0

# For the euro sign part - https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python

# For the prevention of "." and "," I used chatgpt
# Prompt used -  How can I prevent a user from using dots or commas with an if statement? - Answer: You can check if the user input contains a dot (".") or a comma (","). 
# If it does, you can print an error message or handle it however you like. Here's a quick example: 
'''
amount1_str = input('Enter the first amount (in cent): ')
if '.' in amount1_str or ',' in amount1_str:
    print("Please enter the amount in cents without dots or commas!")
else:
    amount1 = int(amount1_str)
'''

# For the Loop - https://www.w3schools.com/python/python_while_loops.asp