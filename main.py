print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input('Are you ready to go?\nWould you like to go left or right?\n').lower()

if direction == "right" or direction == "r":
  sw_wa = input('You just reached the wharf. Would you like to swim to the island in front of you or wait for a while for a  boat?\nType "swim" or "wait"\n').lower()
  if sw_wa == "wait" or sw_wa == "w":
   door = input('Good decision! One more step to find the treasure. There are three doors. Which one would you like to open? Red, green or yellow? Good luck!\n').lower()
   if door == 'green' or door == 'g':
      print("Yesss! You just found the treasure!")
   elif door =='red' or door == 'r':
      print('Fire! Game over')
   elif door == 'yellow' or door == 'y':
      print("No no no! Wrong door, game over")
   else:
     print("Come on! You didn't choose any of the doors, so game over!")
  else:
    print('This water is full of piranha...game over!')
else:
 print('Never go left! Game over!')




# print("Come on! You didn't choose any of the doors, so game over!")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload