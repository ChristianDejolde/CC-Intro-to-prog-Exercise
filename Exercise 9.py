# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:42:19 2024

@author: Christian James
"""

def hello():#hello is created as a function
    print("Hello")  #prints hello 

def main():#main is also created as a function
    hello()  #this calls the hello function to do what its supposed to do

if __name__ == "__main__": #checks if the script is the main function of the code
    main()