# Written by Python3.9
# Programmer: Sh4d0wE4

import random
import time
import os
import sys

try:
    def cleanscreen():
        os.system("cls")

    cleanscreen()
    playername = input("Please Insert Your Name: ")

    cleanscreen()
    print("welcome...")
    time.sleep(1)
    print("please hold on...")
    time.sleep(1)
    cleanscreen()

    print("---------------------------------------")
    print("Number Guessing Game")
    print("Programmer: Sh4d0wE4")
    print("---------------------------------------")

    secim = input("1- Easy\n2- Normal\n3- Hard\nPlease make a choice: ")

    if secim == "1":
        point = 100
        cleanscreen()
        print(f"Dear {playername}, a number from 0 to 10 has been picked up by the computer. please find that number.")
        sayi1 = random.randint(0, 10)

        while True: 
            tahmin = int(input("number: "))

            if tahmin < sayi1:
                point = point - 10
                print("The number estimate you entered is too small. Please try again.")
                continue
        
            if tahmin > sayi1:
                point = point - 10
                print("The number you entered this time is very large. Please try again.")
                continue
        
            if tahmin == sayi1:
                cleanscreen() 
                print("-----------------------------------------------------------")
                print("Congrulations! You Found The Number")
                print(f"Player Name: {playername}")
                print(f"The Number The Computer Holds: {sayi1}")
                print(f"Your Score: {point}")
                print("-----------------------------------------------------------")
                break

    if secim == "2":
        point = 1000
        cleanscreen()
        print(f"Dear {playername}, a number from 0 to 100 has been picked up by the computer. please find that number.")
        sayi2 = random.randint(0, 100)

        while True: 
            tahmin = int(input("number: "))

            if tahmin < sayi2:
                point = point - 10
                print("The number estimate you entered is too small. Please try again.")
                continue
        
            if tahmin > sayi2:
                point = point - 10
                print("The number you entered this time is very large. Please try again.")
                continue
        
            if tahmin == sayi2: 
                cleanscreen()
                print("-----------------------------------------------------------")
                print("Congrulations! You Found The Number")
                print(f"Player Name: {playername}")
                print(f"The Number The Computer Holds: {sayi2}")
                print(f"Your Score: {point}")
                print("-----------------------------------------------------------")
                break

    if secim == "3":
        point = 10000
        cleanscreen()
        print(f"Dear {playername}, a number from 0 to 1000 has been picked up by the computer. please find that number.")
        sayi3 = random.randint(0, 1000)
    
        while True:
            tahmin = int(input("number: "))
        
            if tahmin < sayi3:
                point = point - 10
                print("The number estimate you entered is too small. Please try again.")
                continue

            if tahmin > sayi3:
                point = point - 10
                print("The number you entered this time is very large. Please try again.")
                continue
        
            if tahmin == sayi3:
                cleanscreen()
                print("-----------------------------------------------------------")
                print("Congrulations! You Found The Number")
                print(f"Player Name: {playername}")
                print(f"The Number The Computer Holds: {sayi3}")
                print(f"Your Score: {point}")
                print("-----------------------------------------------------------")
                break

except KeyboardInterrupt:
    print("You Exited the Program!")




