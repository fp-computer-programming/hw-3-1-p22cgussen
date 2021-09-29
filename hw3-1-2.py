# Author CCG 9/28/21

card1 = input("What was your first cards value?")
card2 = input("What was your second cards value?")
sum = int(card1) + int(card2)

if sum >= 21:
    print("You have busted")

if sum <= 21:
    print("You are safe")
