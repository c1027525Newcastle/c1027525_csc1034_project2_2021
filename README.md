#c1027525_csc1034_project2_2021

##Overview of application
The application is mostly run using the Interface.py file where it has the main
function that is used to call all the functions in the Main.py file. Most of the application
revolves around file manipulation more than it does on using classes, except one instance
where a class method is being called to save the NewContact to the Contacts.txt file.

The application can run endlessly as after all the functions are done, the main()
function calls itself and restarts choosing process. To be noted one of the chooses is
to close the application which will stop the main() function from looping.

##Assumption made during the programming cycle of this project
Planning ahead of the actual moment when I started to program the application helps.
My first steps where in drawing a plan of all the functions I would use and how they
would call each other or how I would use the different levels of assumptions  when inputting
data.

A big part in why I had an easy time with file manipulation was that I used some of my
older codes from highschool.

Another assumption I made is that it's hard to think of all the different methods data
can be entered and how to make your code "foolproof" against different input data
(e.g. the user entered a letter where only integers were supposed to be allowed).

##How to run the application
The application can be used smoothly by running the Interface.py file as it acts as an
interface for the application.

The application does not have a CLI thus the only way to use it is the one described up.

##How to use the application with input data
By running the Interface.py file the application has an interface that allows the user to
input what he wants to do with the program. The main() function has loops with
which it calls itself and allows the application to run endlessly. It also offers the
option to stop the application when the user returns to the "main" menu.