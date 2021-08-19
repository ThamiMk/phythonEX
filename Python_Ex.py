from array import *

def is_palindrome(word):
#split the word into individual letter and into "word"
    for words in word.split():
#reverse the letters into variable "rev"
        rev= words[::-1]
#Test is selected word is a palindromee
        if (rev == word):
            print(word + " is a palindrome")
        else: 
            print(word+ " is not a palindrome")

is_palindrome("Thami")
is_palindrome("racecar")
#__________________________________________________

#init array
arr = [1,4,9,16,25]

def doubler(numbers):

# for loop for every element in the array times by 2
    for x in numbers:
            print(x * 2, end=" ")

doubler(arr)
#_________________________________________________
print()

def fizz_buzz(max):

#inti arrays 

    arr2 = [] # array for 4 & 6
    arr3 = [] # array for 4 / 6

# checks each number from 0 to limit
    for num in range(0,max):
        if(num % 4 == 0 and num % 6 == 0):
            arr2.insert(1,num)
        elif (num % 4 == 0 or num % 6 == 0):
                arr3.insert(1,num)
                 
    print(arr3)

fizz_buzz(50)
#___________________________________________________

def average_of_three(num1, num2, num3):

    print("The average of your numbers is: ", end="")
    print((num1+ num2+ num3) / 3)

average_of_three(95,4,20)

#_____________________________________________________

def goodbye(name):
    print("Bye "+name)

goodbye("Thami")