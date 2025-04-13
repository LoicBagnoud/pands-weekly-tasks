'''
squareroot.py

The objective of this program is to take a positive floating-point number as input and outputs an approximation of its square root.

Author: Loic Bagnoud
'''

# I found this nifty function that uses the formula that I learned. Reference at the bottom. I mainly altered the variable names and used division rather than multiplication.
# You have an initial guess that will take one argument called n and divide it by 2. Afterwards, the result will be the actual Newton formula.
# Basically, the initial guess + the argument divided by the initial guess and all of that divided by 2. 

def newtonsqrt(n):
    initial_guess = n / 2 
    result = (initial_guess + n / initial_guess) / 2 

    # This while loop ensures that we keep guessing until the result matches with the initial guess. 
    while result != initial_guess: 
        initial_guess = result
        result = (initial_guess + n / initial_guess) / 2 
    return result


# With the function created, we now move towards creating the user input. First we need to make sure of a couple of things:
# That the user does not use negative or positive integers, negative floats or strings.

# So, we create this loop. We create a variable called user_input and we ask for the user's input
while True:
    user_input = input("Please enter a positive floating point number: ")
    # We then make the following try and make it so that the user's input is automatically assigned a float value. And put it into a variable called corrected_number
    try:
        corrected_number = float(user_input)

        # This makes sure that the user's input is not negative. 
        if corrected_number <= 0:
            print("That is not a positive number. Please try again.")

        # If it's a positive value, we go towards the next check.
        else:
            # Check that the input string includes a decimal point. Just to be extra sure.
            if '.' not in user_input:
                print("Please enter a floating point number with a decimal point (e.g., 5.0).")
            # After all the checks, we assign it to a final variable called final_number and break the loop.
            else:
                final_number = corrected_number
                break
            # If the user inputs strings, we can run this except valuerror and just go back into the loop.
    except ValueError:
        print("That's not a valid number. That is a string. Please enter a positive floating point number.")

# Finally we print everything.
print(f"The square root of {final_number} is approx. {newtonsqrt(final_number)}")


# References: 

# https://www.w3schools.com/python/python_try_except.asp - For the try and except functions

# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756 - The code idea for Newton's method 

# https://www.youtube.com/watch?v=gHL48ePY7lk and ChatGPT - The explanation of Newton's method.
'''
 Prompt used: Can you explain to me in very simple terms what the Newton's square root method is? 
            Also, please explain it for someone who does not understand the concept of square roots so that I see the concepts connect.
            (Didn't include the full explanation here because it doesn't seem relevant. It was for my own understanding)
'''
