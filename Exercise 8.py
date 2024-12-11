# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:42:19 2024

@author: Christian James
"""

names = ["Fin", "Marcus", "Hans", "Romel", "Gwen", "Natasha"] #list of names

listedname = input("What is your name? ")#takes the name of the user
if listedname in names: #checks if the user's name is in the list or not

    print(f"{listedname} is written here, Welcome aboard")#It only prints if the name is there
else:
    print(f"{listedname} is not written in the list, Get out of our ship thank you very much")#It only prints if the name is not there

