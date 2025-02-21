print("Hello World")
print("This is an interesting message")
print('This works as well')

print("Hello from the other file")
print("Another line in second file")

# Arithmetic operations
print(7+11)
print(7-11)
print(7*11)
print(int(9/3))
print(2**10)

print(9%4)
print(8%9)
print(44%9)

print(1 or 2 or 3)
print(1 and 2 and 3)
print(1 and 2 and False and 9)

# Read Me Notes

# This makes the text bigger
## A bit smaller
### Even smaller

# New Paragraph
# This makes the text bigger
## A bit smaller
### Even smaller

# New Paragraph
This is normal text

List:
1. First
2. Second
3. Third
4. Fourth

# Homework 2
# Instructions
# - Given the “gross” salary of a person, calculate the “net”.
# Here are the constraints:
# 1.If the gross is less than 1000, then the income tax is 10%
# 2.If the gross is less than 2000, then the income tax is 12%
# 3.If the gross is less than 4000, then the income tax is 14%
# 4.If the gross is more than 4000, then the income tax is 18%
# 5.If the gross is less than 2000, every child gets you a tax cut of 1%
# 6.If the gross is more than 2000, every child gets you a tax cut of 0.5%
# Read the “gross” and the number of children
# Print the “net”
# Use try/except when reading the inputs '

print("Welcome to Lichtenberger Tax Advisory. Please answer the following questions, so we can create your tax report:")

try:
    gross_salary = int(input("What is your monthly gross salary? (0 Deicmals)"))
    no_kids = int(input("How many children do you have?"))
    if gross_salary < 1000:
        tax_rate = 0.1
    elif gross_salary < 2000:
        tax_rate = 0.12
    elif gross_salary < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18
    if gross_salary < 2000:
        tax_cut = 0.01 * no_kids
    else:
        tax_cut = 0.005 * no_kids
    real_tax_rate = max(tax_rate - tax_cut, 0)
    tax_amount = gross_salary*(real_tax_rate)
    net_salary = gross_salary - tax_amount
    print(f"Your tax rate is {real_tax_rate*100}%. You need to pay the IRS {tax_amount}$. Your monthly net salary is {net_salary}$.")
except ValueError:
    print("Please enter a valid number (Must be an integer).")

# For examples
for i in range(1,10):
    print(i)

s = 0
for i in range(1,11):
    s += i

print(s)

i = 1
s = 0
while i <= 10:
    s += i
    i += 1
print("sum using while is also", s)

# If examples
# Let's create a virtual bartender that serves you if you are of legal age
drinks = ["Whiskey", "Rum","Tequila","Gin","Sake","Wine","Beer","Vodka","Champagne"]
mixers = ["Fanta","Fanta Limon","Red Bull","Tonic Water","Cola","Soda"]

import random

print("I am the virtual bartender, welcome to my bar")
name = input("What should I call you?")

try:
    age = input ("How old are you?")
    age = int(age)
    legal = None
    country = input("Where are you from?")
    if age < 14:
        legal = False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    if legal:
        print(f"Here is a {choice(drinks)} {choice(mixers)}")
    else:
        print(f"I can only serve you {choice(mixers)}")
except ValueError:
    print("I don't have time for your games! Get out!")

#Input examples
name = input("What is your name? ")
age2 = input(f"How old are you {name}? ")
age2 = int(age2)
print(f"{name} based on my advanced calculations, you were born in {2024-age2}")

# Exception examples
name = input("What is your name? ")
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name} based on my advanced calculations, you were born in {2024-age2}")
    7/0
except ValueError:
    print("Please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print("This is another type of error")
else:
    print("Thanks for playing the game as expected")
finally:
    print("Thanks for playing the game")

# While examples
# You have 3 lives. I roll the dice. If I roll 6, you win.
# If not a 6, you lose 1 life.

from random import randint

lives = 3

while lives:
    roll = randint(1,6)
    if roll == 6:
        print("You rolled a six! You win!")
        break
    else:
        print(f"You rolled a {roll}! You lose a life!")
        lives -= 1
        print(f"You have {lives} lives left")

# Simple string examples
s = "Hello"
print(s)
s2 = 'Hello sir #@#ä2e23'
print (s2)
s = ('And she said: "hello!"')
print(s)
print(",.'\"\"\"\"")
s = "hello"
print(s[2], s[4])
print(s[-1])
print(s[1], s[-5])


# Operations examples
s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(s1, "hello")
print(3*s2)

print(s1, len(s1))
print((3*s2), len((3*s2)))
for c in s2:
    print (c)

s3 = ""
for c in s2:
    s3 += (4*c)
print(s3)

print("h" in s1)
print("d" in s2)
print("d" in s3)

# Slices examples
s = "abcdefghijklmnop"
print(s)
print(s[1:4], s[6:9])
print(s[:4], s[6:])
print(s[1:10:2])
print(s[::-1])
print("racecar"[::-1])

# This is how you replace a letter
s ="cat"
s = "r" + s[1:]
print(s)

s ="seven"
s = s[:2] + "7" + s[3:]
print(s)

# Methods examples
print(dir("hello"))
print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK".capitalize())
print("hello".center(50,"x"))
print("gmail.com".find("."))
s = "i see a cat who like to cat while i cat on a cat"

# find all occurrences
pos = 0
while True:
    pos = s.find("cat",pos)
    if pos == -1:
        break
    print("found cat on position", pos)
    pos += 1

# Join

# lower
s = "I SEE A LOT OF THINGS!"
print(s.lower())

# upper
s = "i see a lot of things!"
print(s.upper().capitalize())

# replace - replaces x with y
s = "i see a cat who likes to eat a rat. what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s = "Hello, kind sir! How are you today?"
print(s.replace(",", "").replace(".", "").replace("?","").replace("!",""))

# split
s = "i like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted))

# Random numbers examples
import random

s = 0
for i in range(10):
    s += random.randint(1, 100)
print(s)

# File example write
# lets create a journal

with open('journal.txt', 'a') as journal:
    while True:
        text = input('Enter a journal entry: (press q to quit): ')
        if text == 'q':
            break
        journal.write(text.capitalize() + '\n')

# Mid Term Questions
# Question 1
# State the type

print(type(2+3))
print(type(6/2))
print(type(2!=3))
print(type(print))
print(type(print(2*2)))
print(type("".find))
print(type("bubu"*2))
#print(type("bubu"*(4/2)))
print(type(["abc",2]))
print(type("bubu"*2))

#Question 2
# Indicate result of the following operation
print(2+3)
print6/2
2!=3
5 or 6
[1,2,3].append("John")
"bubu"*2

#Question 3
# Assume the operations are executed in oder. What will each print display
a = 2
b = 3
 len(["abc",2])
2

# Write a function that forces the user to enter a multiple of 6 number. Use try, except to catch invalid inputs. Return that number
def multiple_six():
     """
     Returns a multiple of 6, keeps asking otherwise
     :return: int
     """
     while True:
         try:
             n = int(input("Please give me a multiple of 6: "))
             if n % 6 == 0:
                 return n
             else: print("That's not a multiple of 6")
         except ValueError:
             print("That's not a valid number")

multiple_six()


#Question 4
# Write a function that takes the name of a text file as parameter. Print out the 3-letter words that start with "b".

punctuation = ",.?!'/"

def find_words(filename):
    """"
    Prints 3 letter words starting with b from a text file
    :param filename: The name of file
    :return: None(nothing)
    """
    with open(filename) as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p, " ")
            words = line.split()
            for word in words:
                if len(word) == 3 and word [0] in "bB":
                    print(word)

find_words("input.txt")

# Simple dictionary
d = {} # Empty Dict
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro"}
print(eng_to_spa)
print(eng_to_spa["three"])
eng_to_spa["pineapple"] = "pina"
print(eng_to_spa["pineapple"])
eng_to_spa.update({"yes": "si", "no": "no", "i": "yo", "am": "soy", "cuban": "cubano"})
print(eng_to_spa)
print(f"i know {len(eng_to_spa)} spanish words")

sentence = "i am cuban"
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word]+" "
print(f"{sentence} translates to : {translation})")
print(dir(eng_to_spa))
print(list(eng_to_spa.keys()))
print(list(eng_to_spa.values()))
x = eng_to_spa.pop("pineapple")
print (x)
print(eng_to_spa)

if "car" in eng_to_spa:
    print(eng_to_spa["car"])
else:
    print("Sorry, I don't know this word")

print(eng_to_spa.get("car", "Sorry, I don't know this word"))
eng_to_spa.setdefault("one", "Sorry, I don't know this word")
eng_to_spa.setdefault("monkey", "Sorry, I don't know this word")

# Book exercise
from enum import unique

import requests

link  = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
result = requests.get(link)
print (result.text)

unique_words = {}
lines = result.text.splitlines() # Same as split but we use
punctuation = ",.?!'/"

def create_dictionary():
    for line in lines:
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            word = word.lower()
            if len(word) > 4:
                unique_words[word] = unique_words.get(word, 0) + 1

create_dictionary()

print (unique_words["romeo"])
print (unique_words["juliet"])

freq = list(unique_words.values())
freq.sort(reverse=True)
freq = freq [:10]
print(freq)
print("the most common words are:")
for f in freq:
    for key, value in unique_words.items():
        if value == f:
            print(key)