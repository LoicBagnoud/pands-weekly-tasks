'''
es.py

The objective of this program is to read in a text file and outputs the number of e's it contains.

Author: Loic Bagnoud
'''

# This involved a lot of research and I wasn't sure if we should use the actual Mobydick txt file. I managed to find on github,
# someone who actually had the book as a txtfile. But I structured the code to take any kind of txt file.

# First I imported the os package but I also found out about the sys package that allows us to work with the command line.
import sys
import os

# This little snippet of code was provided by chatgpt. My understanding is that the command line takes 2 arguments. 1 for the python program
# and one for the actual file we're gonna read. So, we're asking it to check if there are more than 2 arguments. If so, than we follow with command. 
if len(sys.argv) != 2:
    print("Usage: python count_es.py <filename>")
    sys.exit(1)  

# This assigns the entire argv argument number 1, in this case the txt file to a variable called filename.
filename = sys.argv[1]

# And this checks the file format. The best way I had to do this was with the ending and endswith function since anything
# that's not a txt file will never end with.txt
if not filename.endswith(".txt"):
    print(f"Warning! The {filename} is not a txt file.")

# This is just to prevent errors if the file does not exist.
elif not os.path.exists(filename):
    print(f"Error. {filename } does not exist.")
    sys.exit(1)

# Then the rest opens the file with the read function enabled.
try:
    with open(filename, "r") as file:
        text = file.read()

# Came back to this task to add this except as it bypasses the error one gets and shows if the file is not found. Also reordered the two ifs above to make sense
# Changed one if to elif to make it conditional.
except FileNotFoundError:
    sys.exit(1)

# A simple .count to count the number of e's
e_count = text.count("e")

# And finally a print to print the number of e's
print(f"The number of e's in {filename} is {e_count}")


# References: 

# Chatgpt for how to use sys.argv and explanation:
'''
Prompt used: I don't understand this: 

                if len(sys.argv) != 2:
                   print("Usage: python count_es.py <filename>")
                   sys.exit(1)

             Can you explain in very simple terms like I understand nothing of python or command lines
'''
# https://gist.github.com/StevenClontz/4445774 - Mobydick txt file

# https://www.reddit.com/r/learnpython/comments/ml39tp/looking_for_a_clear_explanation_on_how_to_use/- Explanation on argv

# https://www.geeksforgeeks.org/python-sys-module/ = Sys Module

# https://www.w3schools.com/python/ref_string_endswith.asp - Checking if the file ends with txt