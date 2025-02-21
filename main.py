# Question 1
# What will be the value of "a" at the end of the code:
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2

print (a)

# Question 2
#What will the following code print?
print((2+3)*6/2 and 18.0)

# Question 3
# Fill in what the code below prints (all the lines):

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

# Question 4
# Here is a function that determines if a number is palindrome or not:
# Which of the below is NOT a palindrome?

word1 = "7489617719749244646336564429479177169847"
word2 = "5485839837501070045005400701057389385845"
word3 = "8025833559061079503003059701609553385208"
word4 = "6593036601359343374664733439531066303956"

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome(word1))
print(palindrome(word2))
print(palindrome(word3))
print(palindrome(word4))

# Question 5
# Write a function that finds all the occurrences of a certain pattern, that starts with “C” has unlimited number of letters and ends with “jeb”
# The function takes 1 parameter: the text to look into and returns the number of matches
# Use only the things we have learned in class. Give some explanations besides the code.

# Additional note: As discussed during the exam, we assume that the words are seperated by spaces.

def pattern_rec(string01):
    """
    :param string01: The string to be analyzed
    :return: Number of occurrences of the pattern
    """
    counter = 0
    # Split the string into words
    words = string01.split()
    for word in words:
        # Identify the pattern start and end
        if word.startswith("C") and word.endswith("jeb"):
            # For every pattern found, the counter is increased by 1
            counter += 1
    return counter

# Test the function with a string that contains the pattern. I put an example below
print(pattern_rec("Carjeb Meanwhile their neighbor Climbjeb who lived near Crankyjeb was busy planting flowers in her garden Catjeb was busy planting flowers in her garden"))

# Question 6
# Please explain what it means that a list is mutable and a string is not mutable (immutable).
# Give some code that shows the difference. Use your own words

#"Mutability" means whether an object can be changed after it is created.
# Lists are mutable, which means their elements can be modified, you can add new elements, or remove existing elements.
# Strings are immutable, which means once they are created, their content can't be changed.
# Below,  is a bit of code that demonstrates this.

## List (mutable)
list01 = [1, 2, 3, 4]
print(list01)

# We can change the first item for example
list01[0] = 5
# Now print again﻿
print(list01)

# We can also add things to the end of the list
list01.append(6)
# Now print again
print(list01)

## String (immutable)
string01 = "hello"
print(string01)

# We can try to change the first letter of the string
# my_string[0] = "H"  # This would be an error: 'str' object does not support item assignment

# However, we can make a new string
string02 = "H" + string01[1:]
# Print both the new and the old string
print(string02)
print(string01)

# Question 7
# Here is some code: Continue by removing the odd numbers from the list.
# Also replace the even numbers with their double value
# Print the list at the end.
# Use only what we have learned in class. Provide some explanation in the form of comments.

import random
random_numbers = []
for i in range (10):
    random_numbers.append(random.randint(1,100))
# I started to continue the code starting here. First, I created a variable "i" that will be used to iterate over the list, as long as "i" is less than the length of the list.
i = 0
while i < len(random_numbers):
    # If the number is even, it is doubled
    if random_numbers[i] % 2 == 0:
        random_numbers[i] = random_numbers[i] * 2
        i += 1
    # If the number is odd, it is removed
    else:
        random_numbers.pop(i)
# Now print the list
print(random_numbers)

# Question 8
# Write a function that checks if the passed parameter is a valid URL or not.
# Please also explain your reasoning. Use only the concepts that we learned in class.
# Do not use any imports

def is_valid_url(url):
    """
    Checks if a URL is valid.
    Because the URL format is quite complex, this function only checks for the following:
    - The URL starts with 'http://' or 'https://'
    - The URL contains no spaces
    - The URL contains a dot
    :param: url (str): The URL string to be validated.
    return: bool: True if the URL starts with 'http://' and contains no spaces, False otherwise.
    """
    if url.startswith("http://") or url.startswith("https://"):
        if " " not in url:
            if "." in url[7:]:  # Skipping 'http://'
                return True
    return False

# Test the function with a URL
url = "htt://www.ie.edu/university/"
if is_valid_url(url):
    print (f"The URL {url} is valid.")
else:
    print (f"The URL {url} is not valid.")

# Question 9
# Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since the day you were born (without counting the days in your birth year and the current year, so just whole years).
# The function takes your birthday as a parameter in string format.
# Do not import anything, use only what we learned in class

def days_since_birthday():
    """
    Calculates the number of days since the birthday. (Or any given date)
    :param: birthday: Format (DD-MM-YYYY)
    :return: Returns the number of days since birthday
    """
    # Split the input birthday string into day, month, and year
    day, month, year = map(int, birthday.split("-"))
    current_year = 2025
    # Calculate the number of full years excluding the birth year and the current year
    full_years = current_year - year - 1

    # Count the number of leap years between the birth year and the current year
    leap_years = 0
    for y in range(year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            leap_years += 1

    # Calculate the total number of days
    total_days = leap_years * 366 + (full_years - leap_years) * 365
    return total_days

# Get the birthday input from the user
birthday = input("Enter your birthday (DD-MM-YYYY): ")
# Print the number of days since the birthday
print(days_since_birthday())

# Question 10
# Upload all your code that you wrote/tested for this exam to your own github account as a PUBLIC repository.
# Share the link to the repository as the answer to this question.
GitHubRepository = "https://github.com/maximltbr/MidTermExam"