#que 1
#What are the types of Applications?
#Applications can be of many types like web apps (YouTube), mobile apps (WhatsApp), desktop apps (MS Word), games (PUBG), and enterprise apps (banking software).

#que 2
#What is Programming?
#Programming is the process of writing instructions that a computer can follow to perform tasks like calculations, automation, or running apps.

#que 3
#What is Python?
#Python is a simple, powerful programming language used for web development, AI, data science, automation, and more.

#que 4
#Program to check if a number is positive, negative, or zero
"""
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
"""

#que 5
#Program to find a factorial
"""
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
"""

#que 6
#Program for Fibonacci series
"""
n = int(input("Enter range: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
"""

#que 7
#How memory is managed in Python?
#Python handles memory automatically using garbage collection, which frees unused memory when variables are no longer needed.

#que 8
#Purpose of continue statement
#The continue statement skips the current loop iteration and jumps to the next one.

#que 9
#Swap two numbers
"""
a, b = 5, 10
temp = a
a = b
b = temp
print(a, b)
"""

#que 10
#Program to check even or odd
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

#que 11
#Program to test whether a letter is a vowel or not
"""
ch = input("Enter a letter: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")
"""

#que 12
#Program to sum of three integers (sum=0 if any two are equal)
"""
a, b, c = map(int, input("Enter three numbers: ").split())
if a == b or b == c or a == c:
    print(0)
else:
    print(a + b + c)
"""

#que 13
#Program to return True if numbers are equal or sum/difference is 5
"""
a, b = map(int, input("Enter two numbers: ").split())
print(a == b or abs(a - b) == 5 or (a + b) == 5)
"""

#que 14
#Program to sum of first n positive integers
"""
n = int(input("Enter n: "))
total = n * (n + 1) // 2
print("Sum:", total)
"""

#que 15
#Program to calculate the length of a string
"""
s = input("Enter a string: ")
print("Length of string:", len(s))
"""

#que 16
#Program to count frequency of characters in a string
"""
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Character frequency:", freq)
"""

#que 17
#What are negative indexes and why are they used?
#Negative indexes in Python mean counting from the end of a sequence. For example, -1 refers to the last element, -2 to the second last, and so on. They are used to easily access elements from the end without knowing the exact length.

#que 18
#Program to count occurrences of a substring in a string
"""
s = input("Enter a string: ")
sub = input("Enter substring: ")
print("Occurrences:", s.count(sub))
"""

#que 19
#Count occurrences of each word in a sentence
"""
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)
"""

#que 20
#Combine two strings and swap first two characters
"""
a = input("Enter first string: ")
b = input("Enter second string: ")
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
result = new_a + " " + new_b
print("Result:", result)
"""

#que 21
#Add 'ing' or 'ly' to a string
"""
s = input("Enter a string: ")
if len(s) >= 3:
    if s.endswith("ing"):
        s += "ly"
    else:
        s += "ing"
print("Result:", s)
"""

#que 22
#Reverse string if length multiple of 4
"""
def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        return s[::-1]
    return s

print(reverse_if_multiple_of_4(input("Enter string: ")))
"""

#que 23
#String made of first 2 and last 2 chars
"""
s = input("Enter string: ")
if len(s) < 2:
    print("")
else:
    print(s[:2] + s[-2:])
"""

#que 24
#Insert a string in the middle of another string
"""
def insert_middle(s1, s2):
    mid = len(s1) // 2
    return s1[:mid] + s2 + s1[mid:]

print(insert_middle("HelloWorld", "Python"))
"""

#que 25
#What is a List? How to reverse it?
#A list is a collection of items in a particular order in Python.
#You can reverse a list using list.reverse() method or list[::-1]

#que 26
#How to remove last object from a list
"""
lst = [1,2,3,4]
lst.pop()
print(lst)
"""

#que 27
#Suppose list1 = [2,33,222,14,25], what is list1[-1]?
"""
list1 = [2,33,222,14,25]
print(list1[-1])
"""

#que 28
#Difference between append() and extend()
"""
lst = [1,2]
lst.append([3,4])  # [1,2,[3,4]]
lst.extend([5,6])  # [1,2,[3,4],5,6]
print(lst)
"""

#que 29
#Largest, smallest, sum from a list
"""
def list_stats(lst):
    return max(lst), min(lst), sum(lst)
print(list_stats([2,33,222,14,25]))
"""

#que 30
#Compare two lists
"""
list_a = [1,2,3]
list_b = [1,2,3]
print(list_a == list_b)
"""

#que 31
#Count strings where length>=2 and first & last char same
"""
words = ["abc","aba","xyz","1221"]
count = sum(1 for w in words if len(w)>=2 and w[0]==w[-1])
print(count)
"""

#que 32
#Remove duplicates from a list
"""
lst = [1,2,2,3,3,4]
unique_lst = list(set(lst))
print(unique_lst)
"""

#que 33
#Check if list is empty
"""
lst = []
if not lst:
    print("List is empty")
else:
    print("List is not empty")
"""

#que 34
#Check if two lists have at least one common member
"""
def common_member(a,b):
    return bool(set(a) & set(b))
print(common_member([1,2],[2,3]))
"""

#que 35
#List of first and last 5 elements squared
"""
squares = [i**2 for i in range(1,31)]
print(squares[:5] + squares[-5:])
"""

#que 36
#Unique elements of a list
"""
def unique_list(lst):
    return list(set(lst))
print(unique_list([1,2,2,3,4,4]))
"""

#que 37
#Convert list of characters to string
"""
chars = ['a','b','c']
s = ''.join(chars)
print(s)
"""

#que 38
#Select random item from list
"""
import random
lst = [1,2,3,4]
print(random.choice(lst))
"""

#que 39
#Second smallest number in a list
"""
lst = [5,1,4,2]
lst_sorted = sorted(lst)
print(lst_sorted[1])
"""

#que 40
#Unique values from list
"""
lst = [1,2,2,3,4,4]
print(list(set(lst)))
"""

#que 41
#Check if list contains a sublist
"""
lst = [1,2,3,4,5]
sub = [2,3]
print(any(lst[i:i+len(sub)]==sub for i in range(len(lst)-len(sub)+1)))
"""

#que 42
#Split list into variables
"""
lst = [1,2,3]
a,b,c = lst
print(a,b,c)
"""

#que 43
#Tuple and difference with list
#Tuple is immutable, list is mutable. Tuple uses (), List uses []

#que 44
#Tuple with different data types
"""
t = (1,"hello",3.5)
print(t)
"""

#que 45
#Unzip list of tuples
"""
lst = [(1,'a'),(2,'b')]
a,b = zip(*lst)
print(list(a), list(b))
"""

#que 46
#Convert list of tuples into dictionary
"""
lst = [('a',1),('b',2)]
d = dict(lst)
print(d)
"""

#que 47
#Create dictionary using tuples
"""
keys = ('a','b')
values = (1,2)
d = dict(zip(keys,values))
print(d)
"""

#que 48
#Sort dictionary by value
"""
d = {'a':3,'b':1,'c':2}
print(dict(sorted(d.items(), key=lambda x:x[1])))  # Ascending
print(dict(sorted(d.items(), key=lambda x:x[1], reverse=True)))  # Descending
"""

#que 49
#Concatenate dictionaries
"""
d1 = {'a':1}
d2 = {'b':2}
d3 = {**d1, **d2}
print(d3)
"""

#que 50
#Check if key exists in dictionary
"""
d = {'a':1}
print('a' in d)
"""

#que 51
#Traverse dictionary
"""
d = {'a':1,'b':2}
for k,v in d.items():
    print(k,v)
"""

#que 52
#Check presence of key
"""
d = {'a':1}
print('b' in d)
"""

#que 53
#Dictionary with keys 1–15
"""
d = {i:0 for i in range(1,16)}
print(d)
"""

#que 54
#Check multiple keys exist
"""
d = {'a':1,'b':2,'c':3}
keys = ['a','c']
print(all(k in d for k in keys))
"""

#que 55
#Merge two dictionaries
"""
d1 = {'a':1}
d2 = {'b':2}
d1.update(d2)
print(d1)
"""

#que 56
#Map two lists into dictionary
"""
from collections import Counter
items = ['a','b','c','d']
values = [400,400,300,400]
print(Counter(dict(zip(items, values))))
"""

#que 57
#Highest 3 values in dictionary
"""
d = {'a':5,'b':2,'c':8,'d':3}
print(sorted(d.values(), reverse=True)[:3])
"""

#que 58
#Combine values in list of dictionaries
"""
data = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
c = Counter()
for d in data:
    c[d['item']] += d['amount']
print(c)
"""

#que 59
#Create dictionary from string
"""
s = "hello"
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
print(d)
"""

#que 60
#Sample string
"""
s = 'w3resource'
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
print(d)
"""

#que 61
#Factorial function
"""
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial(5))
"""

#que 62
#Check number in range
"""
def in_range(num,start,end):
    return start <= num <= end
print(in_range(5,1,10))
"""

#que 63
#Check perfect number
"""
def is_perfect(n):
    return sum(i for i in range(1,n) if n%i==0)==n
print(is_perfect(6))
"""

#que 64
#Check palindrome
"""
def is_palindrome(s):
    return s==s[::-1]
print(is_palindrome("madam"))
"""

#que 65
#Basic types of functions in Python
#Built-in functions and user-defined functions

#que 66
#Pick random item from list/tuple
"""
lst = [1,2,3]
print(random.choice(lst))
"""

#que 67
#Pick random item from range
"""
print(random.choice(range(1,10)))
"""

#que 68
#Get random number
"""
print(random.randint(1,100))
"""

#que 69
#Set starting value in random numbers
"""
random.seed(10)
print(random.randint(1,100))
"""

#que 70
#Randomize items of a list
"""
lst = [1,2,3,4]
random.shuffle(lst)
print(lst)
"""

#que 71
#File function and keywords
#open(), 'r', 'w', 'a'

#que 72
#Read entire text file
"""
with open('file.txt','r') as f:
    print(f.read())
"""

#que 73
#Append text to file
"""
with open('file.txt','a') as f:
    f.write("\nHello World")
with open('file.txt','r') as f:
    print(f.read())
"""

#que 74
#Read first n lines
"""
n = 3
with open('file.txt','r') as f:
    for _ in range(n):
        print(f.readline(), end='')
"""

#que 75
#Read last n lines
"""
n = 3
with open('file.txt') as f:
    lines = f.readlines()
print(''.join(lines[-n:]))
"""

#que 76
#Read file line by line into a list
"""
with open('file.txt') as f:
    lines = f.readlines()
print(lines)
"""

#que 77
#Read file line by line into a variable
"""
with open('file.txt') as f:
    data = f.read()
print(data)
"""

#que 78
#Find longest words
"""
words = ["apple","banana","watermelon"]
print(max(words,key=len))
"""

#que 79
#Count lines in a file
"""
with open('file.txt') as f:
    print(len(f.readlines()))
"""

#que 80
#Count word frequency in file
"""
from collections import Counter
with open('file.txt') as f:
    words = f.read().split()
print(Counter(words))
"""

#que 81
#Write list to file
"""
lst = ['a','b','c']
with open('file.txt','w') as f:
    for item in lst:
        f.write(item+'\n')
"""

#que 82
#Copy file contents to another file
"""
with open('file.txt') as f1, open('file_copy.txt','w') as f2:
    f2.write(f1.read())
"""

#que 83
#Exception handling & Error
#Use try-except. Error stops code execution.

#que 84
#Except statements and built-in exceptions
#Multiple except allowed. Examples: ZeroDivisionError, ValueError, TypeError, IndexError

#que 85
#Else in try-except-else executed if no exception occurs

#que 86
#One except handles multiple exceptions
"""
try:
    x = int('a')
except (ValueError, TypeError):
    print("Error occurred")
"""

#que 87
#Finally block is executed always

#que 88
#'1'==1 returns False

#que 89
#Try/except/finally example
"""
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
finally:
    print("Execution done")
"""

#que 90
#Enter only odd numbers, else raise exception
"""
num = int(input("Enter an odd number: "))
if num % 2 == 0:
    raise Exception("Even number entered!")
else:
    print("Correct input:", num)
"""


