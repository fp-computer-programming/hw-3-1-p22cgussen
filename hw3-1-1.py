# Author CCG 9/28/21

wins1 = input("How many games did team 1 win?")
ties1 = input("How many games did team 1 tie?")

wins2 = input("How many games did team 2 win?")
ties2 = input("How many games did team 2 tie?")

points1 = wins1 * 2 + ties1
points2 = wins2 * 2 + ties2

if points1 > points2:
    print("Team 1 finished with more points")

if points2 > points1:
    print("Team 2 finished with more points")
