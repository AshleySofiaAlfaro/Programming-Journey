#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### LEGEND ###

# SETS - Curly brackets {} - Removes redundancies
var1={"happy", 16, True, "happy"}



# LISTS - Brackets [] - Used to store MULTIPLE VALUES in a single variable; doesn't allow duplicates
var1=["happy", "excited", "joy"]

# CONSTRUCTOR LIST -
var1=(("happy", "excited", "joy"))



# TUPLES - Parentheses () -  Store MULTIPLE values in a single variable; allows duplicates
var6=(("happy", 16, True, "happy"))



# IF-ELSE STATEMENTS


## NESTING DICTIONARY ##
courses={
    "Class_1":{
        "Instructor":"Rylan Chong",
        "Course Number": "CS 202"
    },
    "Class_2":{
        "Instructor":"Helen Turner",
        "Course Number":"DS 101"
    },
    "Class_3":{
        "Instructor":"Mark Speck",
        "Course Number":"DS 201"
    }
};




### OPERATORS ###
# X + Y
12 + 21

# X * Y
3 * 7

# X // Y - Floor divsion rounds down to the nearest number
17 // 13

## Another way of writing operators ##
x=5

# X+=6 or X=5+6
#x+=6
#print(x)

# X*=6 or X=5*6
#x*=6
#print(x)

# X//=6 or X=5//6
x//=6
print(x)


# In[26]:


###########
##Comment##
###########

#Comment
# Comment
# Comment #
#Comment#
#Comment----blahblahblahblah

##This code is about comments and the various styles##

#print("hi")

##Variables##

##Unassigned variables##

#a # - Error result bc no assigned value
#b= # - Error result ^

#Integer vs Float. Float includes decimals.

##Assigned variables##
a=5;
b="Hello class"
c='c'
d="Hello 'Alice' how are you?" # Single quote w/in double quote
e='Hello "Bob" how are you?' # Double quote w/in single quote

'''
Using variables allows you to reuse things over and over. It gets stored in memory.
Downside of using variables is that it can get confusing. Give variable some context.
'''

hello='a'
# How are you=1; Error - Invalid syntax due to spaces
How_are_you=1; #Works
# How-are-you=1; Error - Syntax error
# How.are.you=1; Error - 'How' is not defined. Avoid using periods
How_are_you+=1; #Works
# How_are_you=<1; Error - The ordering is 'wrong'
How_are_you<=1; #Works
How_are_you<1; #Works
# 1How_are_you=1; Error - Syntax error, invalid decimal literal

1==1; # Two equal sign is 'checking'; means 1 equals 1; this is considered a value


# In[47]:


'''
Adding new line of code makes it nonprocedural.
'''
___ = 1;

##Print Function##
print(___);
print('a'); 
print("Hello 'Alice' how are you?");
print('c');
print(7); # Works, even though you never assigned a variable
print(1000); # Works, prints out numbers


# In[55]:


## Assigning MULTIPLE Variables ##

# Traditional
a="oahu";
b="oahu";
c="oahu";

print(a);
print(b);
print(c);

print(a+b); #Works
print("oahu"+" oahu"+" oahu"); #Plus sign '+' represents combining things in a print line
#print(a+1); Error - Don't mix integer and string
print(1+2); #Works, used as numeric, shows '3'
print("1"+"2"); #Works, used as string, shows '12' 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Multiple Variable Assigned to 1 Value - Alt 1
a=b=c="maui";
print(a);
print(b);
print(c);

# One Variable Assigned to Multiple Values - Alt 2
locations=["maui", "oahu", "big island"];
a,b,c=locations;
print(locations);
print(a);
print(b);
print(c);


# In[4]:


### ALL ABOUT STRINGS ###

# TRADITIONAL String #
# print("Welcome"); or print('Welcome');

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# MULTILINE String # - Use triple single/double quotes
a="""Hello everyone!
Today we will be 
talking about multiline
string."""; 

print(a);

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# MODIFYING String #
c="welcome everyone";
e="Welcome everyone2";
s="_";

print(c.capitalize());
print(e.lower());
print(c.upper());
print(c.title());
print(e.strip());
print(c.replace("W", "R"));
print(c.split(","));
print(s.join(c));

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# CONCATENATE String #
a="Welcome"
b="Everyone"
c= a+ " " +b;

print(a+b);
print(c);

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# FORMAT String #
score = 16;
message = "Alice won the game with the score of {}";
print(message.format(score));


# In[ ]:


# Multiple NUMERIC Values w/ NO INDEX # - Con: Have no control
alice_score = 16;
bob_score = 12;
lauren_score = 10;
message = """
Alice won the game with the score of {}. 
Bob was second with a score of {}. 
Lauren was third with a score of {}."""

print(message.format(alice_score, bob_score, lauren_score));


# Multiple NUMERIC Values w/ INDEX #  - Index usually start @ 0
alice_score = 16;
lauren_score = 10;
bob_score = 12;
message = """
Alice won the game with the score of {0}. 
Bob was second with a score of {2}. 
Lauren was third with a score of {1}."""

print(message.format(alice_score, lauren_score, bob_score));

# The order MATTERS when using index - Can't use negative (for this index)

alice_score = 16;
bob_score = 12;
lauren_score = 10;
message = """
Alice won the game with the score of {0}. 
Bob was second with a score of {1}. 
Lauren was third with a score of {2}."""

print(message.format(alice_score, bob_score, lauren_score));


# In[44]:


### ALL ABOUT BOOLEANS ###

# Simple Boolean #
#print(10>16) - Output: False
#print(10==16) - Output: False
#print(10<16) - Output: True

# True Boolean # - Indent matters
a=10

if(a==10):
    print("Value is 10.")
print("Goodbye.");

if(a==10000):
        print("Value is 10.")
print("Goodbye.");

# IF and ELSE statement
a=10
b=16

if b>a:
    print("b is greater than a")
else:
    print("b is less than a");


# In[1]:


### BOOLEAN APPLICATION ###

score=input('Enter your score: ')

#if int(score)>=70:
#    print("You pass the class!")
#else:
#    print("You're almost there to passing the class.")

# Advance Boolean Application #

if int(score)>=70:
    tokens = int(score)
elif int(score)>=50:
    tokens = 5
else:
    tokens = 1
print(f"You won {tokens} token(s) for your score.")


# In[ ]:





# In[2]:


# Advance Boolean Application # - 2
# Make sure to specify data type. Can affect the results.

password = int(input("Enter your password: "))

if (password)==123:
    print("""Correct password. 
    You have access to all my gold and silver!
    Just kidding. It is just rocks.""")
else:
    print("""Wrong password. 
    Please try again to gain access to my rocks.""")


# In[16]:


### Operators ###
# X + Y
12 + 21

# X * Y
3 * 7

# X // Y - Floor division rounds down to the nearest number
17 // 13

## Another way of writing operators ##
x=5

# X+=6 or X=5+6
#x+=6
#print(x)

# X*=6 or X=5*6
#x*=6
#print(x)

# X//=6 or X=5//6
x//=6
print(x)


# In[166]:


# 2/8/2024 & 2/13/24 - NOTES

### LISTS - Used to store MULTIPLE VALUES in a single variable. It uses brackets [] ###
var1=["happy", "excited", "joy"]
var1

var2=[10, 1, 16]
var2

var3=[True, False]
var3

var4=["happy", 16, True]
var4 # - Can mix up string, int, and boolean!


## TYPE and LENGTH of List ##
var1=["happy", "excited", "joy"]
#print(var1)
#print(type(var1)) # - Shows the data type
#print(len(var1)) # - Shows how many values are in the variable


## CONSTRUCTOR Lists ##
var1=(("happy", "excited", "joy"))
#print(var1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

### INDEXING - Method to access a value stored in computer memory ###

## STRING Index ##
var5="happy"
#print(var5[-1])

# H(0) A(1) P(2) P(3) Y(4) #
# H(-5) A(-4) P(-3) P(-2) Y(-1) # - Can't go out of range (Character Limit)

### Indexes of String, Integer, and Mix Lists ###
## STRING List ##
var6=["happy", "excited", "joy"]
#print(var6[-2])

## INTEGER List ##
var7=[10, 1, 16]
#print(var7[2])

## MIX List ##
var8=["happy", 16, True]
#print(var8[2])

# : represents the set of values you want to grab

var9=["happy", 10, True, "excited", 1, False, "joy", 16] 
#print(var9[0])
#print(var9[0:3]) # This means up to 3. Number AFTER colon isn't included.
#print(var9[1:])
#print(var9[:4])
#print(var9[0], var9[3], var9[5], var9[-7]) # Grabbing individual values

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

## Changing VALUES in a List ##
# V1 #
var9[1]="lucky"
#print(var9)

#var9.insert(1, "lucky") # Doesn't replace. Just inserts into list and creates new index.
#print(var9)

# Changing Multiple Values #
var9[1:3]=["satisfied", 12]
#print(var9)

# Adding 2 Values #
var9[6:7]=["delighted", "cheerful"]
#print(var9)

# Adding 1 Value #
var9[1:3]=["merry"] # - Use brackets!!!
#print(var9)

# Append - Puts a value at the END
var9.append(5) 
#print(var9)
#var9.append([5, 6, 7]) - Can do multiple values, but puts it into ONE index.

# Extend - Adds MULTIPLE values to the END of list
var9.extend(["Extended", "List", "of", "Words"])
#print(var9)

# Remove Specific Value in a List #
var9.remove("Extended")
#print(var9)

# Remove Specific Value Using Pop #
#Control Pop
var9.pop(8) # Can't do multiple values.
#print(var9)

#Uncontrol Pop
var9.pop() # Gets rid of the value at the end.
#print(var9)

## Delete ##
del var9[0]
#print(var9)

del var9[7]
#print(var9)

#del var9 - Error: 'name 'var9' is not defined.' It's not defined because it no longer exists.
#print(var9) 

#var9.clear() # List still exists as an object, but removes all the values.
#print(var9)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

### Sort List ###
var10=["Merry", "Excited", "delighted", "cheerful", "Of"]
var11=[16, 100, 1, 12, 84]
var99=["Merry", "excited", "16", "100", "0", "20", "Lion", "hawaii", "RICHARD", "cade"] 
print(var10)
print(var11)

## Joining ##
var12=var10+var11 # Order matters. Can do replications of lists - 'var12=var11+var11+var11'
print(var12)

#var10.extend(var11)
print(var10)

## Sorting ##
var11.sort() # Can only sort PURE string/integer. If both in the same list, it will show an error.
print(var11)

var10.sort()
print(var10)

var99.sort() # Not perfect. Takes capitalization into account; upper first, then lower.
print(var99)

# Reverse Sort #
var10.sort(reverse=True)
print(var10)

var11.sort(reverse=True)
print(var11)

# Sort Keyword #
var10.sort(key=str.lower)
print(var10)

# Reverse Sort 2 #
var11.reverse()
print(var11)


# In[131]:


### TUPLES - Store multiple values in a single variable ### - Uses parentheses 

# Tuples allow duplicate values 
var6=(("happy", 16, True, "happy"))
print(var6)

print(len(var6)) # Shows how many values are in the variable
print(type(var6)) # Is this variable a list, tuple, set, etc?

# Unpacking Tuple - Extracting values back into the variable
# Packing Tuple 

## Joining 2 Tuples ##
var1=("happy", "excited", 12)
var2=("joy", 16, 10, True, "satisfied", "cool")
var3=var1+var2
var4=var2+var1
print(var3)
print(var4)
print(var2[1])

# The plus (+) and multiplication (*) are the only ones that seem to work.

var5=var1*2 #Prints var 1 twice
print(var5) 


# In[79]:


### SETS - Removes any redundancies ###

## Basic Set ##
var1={"happy", 16, True, "happy"}
print(var1) #Duplicates get ignored

## Length and Type Function ##
print(len(var1))
print(type(var1))

## Accessing Set - Keyword: in ## - Asking if certain value is in the variable.
print(16 in var1)
print("sad" in var1)

## Adding Values ##
# Add ONE Value #
var1.add("joy")
print(var1)

# Add Set #
var1={"happy", 16, True}
var2={"excited", 10, False}
var1.update(var2)
print(var1)

# Add a List with a Set # - It's possible to combine, but the .update only works w/ SET
var1={"happy", 16, True}
var3=["excited", 10, False]
var1.update(var3)
print(var1)

# Add a Tuple with a Set # - Also works with tuples!
var1={"happy", 16, True}
var3=("excited", 10, False)
var1.update(var3)
print(var1)

# Remove a Value #
#var1.remove("happy")
#print(var1)

# Discard a Value #
#var1.discard(16)
#print(var1)

# Pop a Value #
var4=var1.pop()
print(var4)
print(var1)

# Clear #
#var1.clear()
#print(var1)

# Delete - Shows an error because it doesn't exist anymore
#var1={"happy", 16, True}
#del var1
#print(var1)


# In[130]:


### DICTIONARY ### Note to self - Everything in dictionary is case sensitive

## Access 1 ##
dictionary_1={
    "Instructor":"Rylan Chong",
    "Course Number":"CS 202",
    "Credits":3,
    "Semesters":["Fall", "Spring", "Summer"]
}

x=dictionary_1["Instructor"] # This calls a particular label to store the value in temporary varaible "x" 
print(x)
y=dictionary_1.get("Instructor") # Another way to call a particular label using 'get' function
print(y)
z=dictionary_1.keys() # Getting the list of keys
print(z)
a=dictionary_1.values() # Getting the list of values
print(a)
b=dictionary_1.items() # Getting the list of items (both keys AND values)
print(b)

## Changing Values ##
print(dictionary_1)

#dictionary_1["Credits"]=2
#print(dictionary_1)

#dictionary_1.update({"Credits":1})
#print(dictionary_1)

dictionary_1["Location"]="Henry 104" # Adding a new label
#print(dictionary_1)

dictionary_1.update({"School":"NSM"}) # Another way to add a new label
#print(dictionary_1)

## Pop A Specific Value ## - Needs an argument/condition
dictionary_1.pop("Semesters") 
print(dictionary_1)

## Pop or Remove LAST Inserted Item ##
dictionary_1.popitem() 
print(dictionary_1)

## Delete or Remove a Specific Key ## 
del dictionary_1["Course Number"]
print(dictionary_1)

## Delete or Remove Dictionary ##
#del dictionary_1
#print(dictionary_1)

## Nesting Dictionary ##
courses={
    "Class_1":{
        "Instructor":"Rylan Chong",
        "Course Number": "CS 202"
    },
    "Class_2":{
        "Instructor":"Helen Turner",
        "Course Number":"DS 101"
    },
    "Class_3":{
        "Instructor":"Mark Speck",
        "Course Number":"DS 201"
    }
};

print(courses)

x=courses.get("Class_2")
print(x)


# In[143]:


### PRACTICE ###

bluebell_flower={
    "Kingdom":"Plantae",
    "Order":"Asparagales",
    "Family":"Asparagaceae",
    "Genus":"Hyacinthoides",
    "Species":"H. non-scripta"
};

bluebell_flower.update({"Color":"Blue"})
print(bluebell_flower)

# Adding a LIST to a SET
set1 = {"DSC", 30, True}
list1 = ["Python", 20, False]

set1.update(list1)
print(set1)

# Inserting a new value into a TUPLE
greetings1=("Hello", "Aloha", "Goodbye")
y=list(greetings1)
y[1]=1000

var2=tuple(y)
print(var2)

# Calling the value in index 1
fruit=["apple", "orange", "banana", "lime", "blueberry"]
print(fruit[1])


# In[30]:


### IF-Else, While, and For Loops ###

## If-Else
var1=10
var2=16

#if var2>var1:
    #print("Ashley")
    #print("var2 is greater than var1")
#else:
    #print("End")

# One-Line Statement Works (Not traditionally done)
var1=10
var2=16
print("var2 is greater than var1") if var2>var1 else print("var1 is less than var2")

## AND If-Else - Both has to be true
var1=12
var2=16
var3=7
if var1>var3 and var2>var1: #Has to be both TRUE statements. Both FALSE doesn't work.
    print("Both conditions are true.")
else:
    print("There is at least 1 false.")

## OR If-Else - At least one has to be true
var1=12
var2=16
var3=7
#if var1>var3 or var2<var1: 
    #print("At least 1 condition is true.")
#else:
    #print("Both conditions are false.")

## Nested If-Else
var1=12
var2=10

if var1>9:
    print("var1 is greater than 9.")
    if var2>9:
        print("var2 is greater than 9.")
    else:
        print("var2 is not greater than 9.")

## While Loop
# Basic While Loop
var1=0
while var1<2:
    print(var1)
    var1=var1+1

# While Loop String List
list1=["happy", "joy", "excited", "merry"]
index=0

while index<len(list1):
    words=list1[index]
    print(words)
    index += 1 # Make sure to add the index or else it would continue to loop in the bg

#list1=[1, 2, 3, 4, 5]
#index=0

#while index<len(list1):
    #numbers=list1[index]
    #print(numbers)
    #index += 1

# Looping and try to identify what numbers are even and what numbers are odd
list2=[1, 7, 12, 16, 105]
index=0

while index <len(list2):
    num=list2[index]
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
    index += 1

## For Loop - Goes through values, puts values into temporary variable, then prints it out
islands=["maui", "oahu", "molokai"]

#for x in islands:
    #print(x)

for x in range(len(islands)): # Using the index to pull the values into the print
    print(islands[x])

# Break Out of Loop - Search feature; goes until it reaches what 'x' equals to
#for x in islands:
    #print(x)
    #if x=="oahu":
        #break # Stops when reaches 'oahu'

for x in islands: # Only prints out 'maui' because it breaks at 'oahu'
    if x=="oahu":
        break
    print(x)

for x in islands:
    print(x)
else:
    print("no moa values left") # Using for loop as 'if' statement
    
num=[100, 101, 102, 103, 104, 105]
for x in num:
    print(x)
    if x==103:
        break # Stops when reaches '103'

## Nested For Loop
index=[0, 1, 2]
islands=["maui", "oahu", "molokai"]
alphabet=["a", "b", "c"]

#for x in index:
    #for y in islands:
        #for z in alphabet:
            #print(x,y,z)
            
## Parallel For Loop - Using 'zip' function
index=[0, 1, 2]
islands=["maui", "oahu", "molokai"]
alphabet=["a", "b", "c"]

#for x,y,z in zip(index, islands, alphabet):
    #print(x,y,z)

## For Loop using Enumerate
for index, x in enumerate(islands):
    print(index, x)


# In[37]:


index = [0,1,2,3]
list1 = ["data science", "computer science", "cybersecurity", "digital forensics"]

for x in index:
	for y in list1:
		print(x,y)


# In[17]:


### FILE HANDLING ###

#file = open("test.txt")
#for x in file:
    #print(x)
#print(file.read())
#print(file.read(3)) - Reads first 3 characters.
#print(file.readline())

file = open("test.txt", "w")
file.write("This text will be overwriting file.")

file = open("test.txt", "r")
print(file.read())


# In[ ]:




