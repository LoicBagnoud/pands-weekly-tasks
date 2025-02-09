# bank.py
'''
The objective of this program is to prompt the user to input two ammounts in cents and sum up the results, 
printing out the result in a human readable format with a euro sign and decimal point between the euro and cent of the amount
'''
# author: Loic Bagnoud

#First I went ahead and made two prompts (making sure they are integers) for the values in cents
ammount1 = int(input('Enter the first ammount(in cent): '))
ammount2 = int(input('Enter the second ammount(in cent): '))

# I went ahead and summed up the ammounts, dividing them by 100. I made sure to use brackets so that the division goes first
result = (ammount1/100) + (ammount2/100)

'''
I struggled with this but I took it in parts. I tried to first assign a variable called txt and formatted the string to display the result (2 decimal points up) and 
then researched how I could present the euro sign. References in the bottom.
'''

txt = f"The sum of these is {result:.2f}%s"%u"\N{euro sign}"

print(txt)



# For the {result:.2f} part - https://www.w3schools.com/python/python_string_formatting.asp#gsc.tab=0
# For the euro sign part - https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python