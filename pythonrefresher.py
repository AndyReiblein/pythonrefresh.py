#Variables,strings, ints, and print
name = "Andrew"

age = '23'

sentence = ("Hi my name is {} and I am {} years old".format(name,age))

#If statements and comments

if int(age) > 18:
    print(sentence)

else:
    ('You are younger than 18')   

#to add comments punch the hash button 

"""with multyline comments
you can use this"""

year = 2002

if int(year) < 2000-2100:
    print("Welcome to the 21st century!")
    
else:
    print("You are before or after the 21st century")    

def hello(name, age):
    print("Hello {} you are {} years old".format(name, age))

hello("Andrew",15 )    

"""Come back to exercise 6 Functions
Q:Create a function named trippleprint that takes a string as a parameter and prints that strings
3 times in a row. So if i passed in the string 'hello' it would print 'hellohellohello'

A:"""

#lists

dognames = ["Fido", "Sean", "Sally", "Mark"]

#add names to list

dognames.insert(2,"Billy")

print(dognames)
#To print specific name use[] eg. print(dognames[3])

print(len(dognames))





    
    

  


     
