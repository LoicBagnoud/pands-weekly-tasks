# pands-weekly-tasks

All exercises are in their appropriate folder. 

## Description of the Exercises

### Week 1

I included this exercise __(hello world script)__ in the folder called Week 1. I know it's not evaluated but we were asked to include it in the weekly-tasks repository. As such I made a little folder for it. It's mainly there for organisation anyway. 

### Week 2
>
For this task, I first approached it with the basic solution of simply taking the values and computing everything. I prompted the user, converted their input to integers, summed both values, and divided by 100. Then I printed the output with the euro sign (something I had to research to understand how to do).
>
Later, I revisited this and added a way to prevent user mistakes, such as using dots or commas. I did this with a __while__ loop and __if/else__ statement: we ask the user to input something (which is initially a string), then check it before converting to an integer. If they include a dot or comma (i.e., a non-digit), the code detects it and asks them to correct it. It only converts to an integer once the input is valid. 

### Week 3

This one, the main objective is to work with the account number that the user provides. It's not made to work with strings or letters but only numbers. I thought on how to best approach this and after several discussions on __Stack overflow__, I found a solution. Unfortunately, the solution provided didn't really work, so I just went ahead and proceeded with creating a variable and following the logic of "X" multiplied by the length of numbers that user imputs - 4 (because we want to show the last 4) and then we sum or concetenate that with what the user created - 4.
>
I then added a simple function with a __while__ loop to prevent the user from entering letters. I achieved this with the __.isdigit()__ method, which was incredibly helpful (and new to me).

### Week 4

This was a very interesting task which had me investigating what was the __Collatz__ function and how it worked. Learning the mechanics of it really helped build the code.
If we look at the code, we can see that it's working to take anything besides 0 (Because you can't really work with 0. I know the collatz can go into the negatives but that's 
beyond the scope of this task). I also made sure that 1 is also accepted. While it doesn't initiate the __Collatz__, I thought it should still be able to print it anyway. 
> 
I was getting a bug where if a negative number was input, followed by any positive number, I would get a list containing the negative number plus our __Collatz__ calculation. The solution was to initialise the list after the loop, so we only append positive numbers.

### Week 5

With this task, my work was made easy with the __datetime__ package that comes with Python. We simply created a variable called today and added the __datetime__ package to it with _(today)_. Then we just add a simple condition that prints a statement if it's a weekday and another statement if it's the weekend. 

### Week 6

This task, much like __task 4__ had me investigating the mathematical concept of __Newton's Squareroot Calculation Method__. After researching this and understand how it works, I was able to find another persons' approach to it in Python and adapted it to my own style. Changed the variable names and used division which is closer to the original equation. 
>
With the function created, I then moved on to to actual user imput and creating all of the conditions that prevented the user from making any mistakes such as using strings or integers. I created a __while__ loop with all the __if/else__ statements as well as __ValueError try/except__ function. Once all the checks are made, we store that in a variable called __final_number__ and we process this variable through the Newton function, printing our final result. 

### Week 7

I had a lot of trouble for this task. The first part was finding the __Moby Dick__ book as a txt file. I just found a user on github that provided that. Once I had that and included it in the same folder as our script, I moved on to the coding itself. After a lot of research running codes from the command line as well as the __sys package__, I finally understood how it works. I call it and structure the number of arguments I want; in this case, it's 2. Once the arguments have been made, I stored it in a variable and I worked with that.
>
Next, come the conditions. I created a condition for the file in case it was not a __txt__ file and in case it didn't exist to begin with. All of this before checking the number of e's with __text.count__ or even read it with the __"r" function__.
> 
The code broke down several times because of how I wanted to check the conditions. I noticed that checking if the file was there to begin with always came first before anything and bypassed any checks of it even being a __txt file__. As such, I went through stages. I began with checking if it's a __txt file__ (could be a __pdf__ for instance) with the __endswith__ function. This guarantees the check works. Then, if the file is not there (in this case, exclicitly the variable we stored before that must be in the same folder) it will print a statement warning the user that the file was not there. I also have the __except FileNotFoundError__ to make sure the user doesn't see that error since it looks messy.
> 
After all of this is done and accounted for, then I can open the file with the __read function__ and check for the number of e's.

### Week 8

The main issue with this task was understanding the equation. I found that making plots is a very interesting thing and its complexities mostly lie on how you want it to look. In other words, I spent more time tweaking the appearance(thanks to __matplotlibs__ documentation on that) than actually writing the code to be functional. 
>
Overall, we import the packages and we make sure our variable random results and the equation make sense. Afterwards, it's mainly bringing up the built in functions of __matplotlib__
and working with the __labels__, the __colours__ and the __legends__. Then it's simply saving it to __png__ files. 