print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island game.")
print("Your mission is to find the treasure.")
direction = str(input("in-front of there is two direction  click right 'R' and left 'L'\n")).upper()
if direction == "R":
    print("you select correct one and you reach to 2nd stage of level")
else:
        print("sorry you select wrong one please start again")
        exit()
secound_stage = input("in-front of there is water lake.what you do either you swim or wait.chose one please click s for swim and w for wait\n").upper()
if secound_stage == "W":
    print("wait is correct one to pick. you reach third stage please select carefully")
else:
        print("you choose wrong one to swim. please start game again")
        exit()
third_stage = int(input("in this third stage in-front of 4 door. door no 1,door no 2,door no 3,door no 4.choose one of these door.click 1,2,3,and4\n"))
if third_stage == 2:
    print("welcome to the last stage of the game")
else:
    print("you pick wrong door.please start agin")
    exit()
fourth_stage = input("please choose two in this five key A,C,D,S,M.and type that two latter's\n").upper()
if fourth_stage == "SA" or fourth_stage == "AS":
    print("your win this game.")
else:
    print(" you pick wrong one.please start again")








