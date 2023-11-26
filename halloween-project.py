#Emily's Holloween Project
#Emily Topete
#It's holloween and you are a character who takes your sister out trick-or-treating. During the day you have to make some choices.
import sys
import time
def print_slow(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)
    
print("\n\nWelcome to Emily's Holloween Chose Your Own Adventure Story!")
time.sleep(2)

print_slow("\n\nThe date is October 31st, 1984 and your 16 years old. Your mother and father are both at work so you have to take your 8 year old sister out to go trick-or-treating.")
time.sleep(2)
input("\n\nPress Enter to continue...")

print_slow("\nYou are standing behind your sister who is sitting down on a chair, as you try to recreate the 2 buns that Princess Leia has.")
input("\n\nPress Enter to continue...")

print_slow("\nYou keep messing with her hair for a while before you notice that it's starting to get dark outside.")
time.sleep(2)

print_slow("\n\nYou look down at yourself to discover that you managed to get hair gel all over your favorite band t-shirt. To buy youreslf some extra time you ask your sister to find a pillow case to collect candy in, and you walk to your room.")
time.sleep(2)
print_slow("\n\nAs you're walking back from your bedroom after putting on a new shirt you hear a doorbell ring.")
input("\n\nPress Enter to continue...")

print_slow("\nYou hear your neighbor's dog bark as you walk closer to the door. You look out the peephole see trick-or-treaters.")
time.sleep(2)
while True:
  choice1 = input("\n\nYour first choice. Do you A want scare the children or B give them candy? (Enter A or B)")
  if choice1 == "A":
    print_slow("\nYou put on a mask of Freddy Krueger that you have, grab some utensils and put them inbetween your fingers, and you open the door.")
  time.sleep(2)
  print_slow("The childen at the door scream and run   away with tears as you chase them down the driveway, many of them dropping their candy bags. You collect their bags and bring them inside. You are a little upset of how light the bags are but that was just because the night just begun.")
  break
  if choice1 == "B":
    print_slow("You call for you sister to bring you the candy bucket as you go to the door to answer it. You sister comes running to the door excited for the night to begin. She gives some candy to each of the childen and even a dog dresses as Frankenweenie.")
    break
else:
  print("\n Incorrect, try again.")
input("\n\nPress Enter to continue...")
print_slow("\nAfter waiting a bit you dicide to take your sister out. You then take a photo with Erica and put the camera back inside before ging out.")
time.sleep(1)
print("\n\n┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌██┘┌┘█┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘███┘┌┘┌┘\n┘┌┘┌┘┌┘┌██┘┌┘┌█┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌\n┌┘┌┘┌┘┌┘█┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘┌██┘┌┘██┌┘┌┘\n┘┌┘┌┘┌┘┌█┌┘┌┘┌██┘┌┘┌┘┌┘┌┘┌┘┌┘█┘┌┘┌┘█┘┌┘r\n┌┘┌┘┌┘┌██┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌█┌┘┌┘\n┘┌┘┌┘┌┘██┌┘┌┘┌██┘┌┘┌┘┌┘┌┘┌┘┌█┌┘┌┘┌██┘┌┘┌\n┌┘┌┘┌┘┌┘█┘┌┘┌██┘┌┘┌┘┌┘┌┘┌┘┌┘█┘┌┘┌┘██┌┘┌┘\n┘┌┘┌┘┌┘┌██┘┌███┌┘┌┘┌┘┌┘┌┘┌┘┌██┘┌┘┌█┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌██┘███┘┌┘┌┘\n┘┌┘┌┘┌┘┌████┘┌┘┌┘┌┘┌┘┌┘███████████┘┌┘┌┘┌\n┌┘┌┘┌┘┌██████┘┌┘┌┘┌██████████████┘┌┘┌┘┌┘\n┘┌┘┌┘████┌███┌┘┌┘███████┘┌┘██████┌┘┌┘┌┘┌\n┌┘┌┘████┌┘███┘┌┘████┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌┘\n┘┌┘████┌┘┌████┘███┘┌┘┌┘┌┘┌┘┌███┌███┌┘┌┘┌\n┌┘███┘┌┘┌████████┘┌┘┌┘┌┘┌┘┌┘██┌┘┌███┌┘┌┘\n┘┌███┌┘┌┘██┌████┘┌┘┌┘┌┘┌┘┌┘┌██┘┌┘┌██┘┌┘┌\n┌┘┌███┌┘┌██┘┌██┘┌┘┌┘┌┘┌┘┌┘┌███┌┘┌┘███┘┌┘\n┘┌┘┌██┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘███┘┌\n┌┘┌┘███┘┌██┘┌┘┌┘┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌┘██┌┘\n┘┌┘┌┘██┌┘██┌┘┌┘┌┘┌┘┌┘┌┘┌██████┘┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌┘┌┘████┌┘██┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘████┌┘┌┘┌┘┌┘███┘┌┘┌███┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌┘███┘┌┘┌┘┌██┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘██┌███┌┘┌█████┌┘┌┘┌┘██┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌┘██┌██┘┌┘██████████┌┘██┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘┌█████┌┘┌┘┌┘┌██████████┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌┘████┌┘┌┘┌┘┌┘███┘┌██████┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘████┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌█████┌┘┌┘┌┘┌┘┌████┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘█████┘┌┘┌┘┌┘┌██████┘┌┘┌┘┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌██┘██┌┘┌┘┌┘┌┘██┌┘███┘┌┘┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘██┌██┘┌┘┌┘█████┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘r\n┌┘┌┘┌┘┌██┘██┌┘┌┘┌┘███┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌┘┌┘┌┘███┘┌┘┌┘┌┘┌┘┌┘┌\n┌┘┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘\n┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌\n")
input("\n\nPress Enter to continue...")

print_slow("\nYou've been walking up and down your neighborhood for hours. You dicide that because Erica's candy bag is almost filled to the brim, that it is time to go home.")
time.sleep(2)
print_slow("\nWhile walking home you notice some what looks to be teenagers TP-ing a house as well as smuching pumkins. You remember this house as being the house that just got sold to a older elderly couple.")
time.sleep(2)
while True:
  choice2 = input(
    "\nShould You either A join, B ignore what is happening, or C call the police? (Enter A, B, or C)"
  )
  if choice2 == "A":
    print_slow("\nYou decided to join in. You walk up to the house with your sister try to pass some toliet paper to your sister to throw on the tree in the front yard. When you went to grab the toilet paper, one of the teenagers walks up to you guys.\n\nWhen they got closer you noticed it was one of your friends from your social studies class. You guys say hi and they pass you the toilet papper to help decorate the house.\n\nAfter a while you notice headlights from a car, as it's getting closser you all decide to run to your house to not get caught.\n\nOnce at your house your sister shares all her candy with everyone and you guys all watch a scary movie together.")
    break
  if choice2 == "B":
    print_slow("\nYou decided to preten nothing happened and walk home.")
    break
  if choice2 == "C":
    print("You dicide to call the police and be a buzz kill. As you are calling the police you and your sister walk home.\n\nIn 4th period the next day you don't see your friend, you think to yourself that they must be sick. For the following week they are still out of class and then you start to hear rumors in the halls. One of the rumors claiming that they were in juvi as they and a group of friends tresspassed, littered, and committed criminal mischief.\n\nYou decide to look into these claims and go to their house to see them. Once at there house you ring the doorbell, after waiting for about a minute their mom answers the door.\n\nThe mom then tells you that those claims are all true and happened on holloween.")
    break
  else:
     print("\n Incorrect, try again.")
print("\n\n\n༼ つ ╹ ╹ ༽つTHE END")
