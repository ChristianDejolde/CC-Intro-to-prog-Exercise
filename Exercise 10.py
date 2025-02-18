# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:42:20 2024

@author: Christian James
"""

def number(value): #creates a function
    if value % 2 == 0:#checks if the number can be divided by 2 until 0 (checks if the number is odd or even)
        return f"{value} is even."#prints if the number is even
    else:
        return f"{value} is odd."#prints if the number is odd

def main():#creates a function
    user_input = int(input("Enter a number: "))#gets user input
    result = number(user_input)#the result takes the number from the previous function
    print(result)#prints the result of the script

if __name__ == "__main__":
    main()#checks if the script or the code is being executed directly