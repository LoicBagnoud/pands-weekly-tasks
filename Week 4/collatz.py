'''
accounts.py

The objective of this program is to ask the user to input any positive integer and outputs the successive values of the following calculation.
At each step, it calculates the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
When the current value is 1, the program ends.

Author: Loic Bagnoud
'''

# This was a bit tricky and I researched stack overflow for ideas on this. But since they all used complex methods, I wanted something more simple.
# The first part is a simple prompt for the user to input their number.
collatz_attempt = int(input("Please input your collatz attempted number: "))

# I created this while loop to make sure that the user does not input a negative nummber or a 0 (since a 0 can't even initiate the loop). I made sure the loop is in place before
# the list because otherwise, any negative number is added to the list. We need to make sure no unwanted numbers get added in. 
while collatz_attempt < 1:
    print("Please make sure you do not use 0 or a negative number. Use a positive number")
    collatz_attempt = int(input("Please input your collatz attempted number: "))

# I created a list for the collatz calculations to be stored. I will print out this list later on. (Made a small correction here to account for the user using 1.)
collatz_list = [collatz_attempt]

# I had to figure out how to check if something was an even number. This helps with that. At first I tried creating multiple alternative variables but I ended up confused with it,
# so I tried just working on the same variable as everything just gets stored in the same place. 

# So basically, if whatever the user input is not 1 (since dividing it by 2 gets you floats and I opted to not work with that) make sure it's an even number and store it
# in what the user wrote. Afterwards, just append it to the list. Otherwise, just multiply it by 3 + 1 (anything that's not an even number will be an odd number). Append it to
# the list afterwards.
while collatz_attempt != 1:
    if collatz_attempt % 2 == 0:
        collatz_attempt = collatz_attempt // 2
        collatz_list.append(collatz_attempt)

    else: 
        collatz_attempt = collatz_attempt * 3 + 1
        collatz_list.append(collatz_attempt)
    
#Finally, when collatz_attempt becomes 1, terminate the loop and print the entire list
print(f"Your collatz attempt ended. Here are your numbers: {collatz_list}")
    
        
# References: 

# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff - Ideas for collatz

# Chatgpt for correction - He mentioned that I needed to store the calculations somewhere to then append them to the list:
# collatz_attempt = collatz_attempt // 2 - This was his proposal and it was very helpful since the code was always breaking.

# https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/ - How to identify Odd numbers.