# pands-weekly-tasks

All exercises are in their appropriate folder. 

## Description of the Exercises

### Week 2
>
For this task, I first approached it with the basic solution of simply the values and computing everything. This was achieved with prompting the user
and just converting that to an integer and summing up both values divided by 100. Then, it was simply printing the output with the euro sign (something I had to reseaarch to understand how to do). Some time later, I went back to this and an additional way of preventing user mistakes, such as the use of dots or commas.
>
This was achieved with a While and if/else statement. We ask the user to input something, whatever he inputs will be a string and then converted into a integer and we go from there. 
If he uses a dot or comma (which is a string) the code will pick that up and ask him to correct it. It will only move to convert things to an integer once the correct value is put. 

### Week 3

This one, the main objective is to work with the account number that the user provides. It's not made to work with strings or letters but only numbers. I thought on how to best approach this and after several discussions on Stack overflow, I found solution. Unfortunately, the solution provided didn't really work, so I just went ahead and proceeded with creating a variable and following the logic of "X" multiplied by the length of numbers that user imputs - 4 (because we want to show the last 4) and then we sum or concetenate that
with what the user created - 4.
>
I then went back to this to add a simple function with a while loop that prevents the user from using letters. I achieved this with the .isdigit function which was incredibly helpful and I wasn't aware of. 

### Week 4

This was a very interesting task which had me investigating what was the collatz function and how it worked. Learning the mechanics of it really helped build the code.
If we look at the code, we can see that it's working to take anything besides 0 (Because you can't really work with 0. I know the collatz can go into the negatives but that's 
beyond the scope of this task). I also made sure that 1 is also accepted. While it doesn't initiate the Collatz, I thought it should still be able to print it anyway. 
> 
I was getting a small mistake where if a negative number was input, followed by any positive number, I would get a list containing the negative number plus our collatz calculation.
The solution was mainly making sure to put the after the while loop so we don't add anything to it that we don't want. This ensures that the collatz is printed properly at the end.

### Week 5

### Week 6

### Week 7

### Week 8