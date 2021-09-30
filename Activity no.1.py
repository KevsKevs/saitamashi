import random
#sample text-based game with simple conditional statement
character_health = 100
icedragon_health = 100
hydra_health = 10000
character_power= 25
item = ""

name = input("Enter your name: ")
print("Hello " + name)

while character_health > 0:
    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select [1 to heal/ 0 to ignore]")
        if n == "1":
            character_health += 10
            print("Your character's health is back to " + str(character_health))
        else :
             print("Your character's health is back to " + str(character_health))
        

    v = int(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 if you want to fight monster in the dungeon \nInput: "))
   
    #Start of Journey
    if v == 1: 
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance > 6:
                item = "Fish"
                print("You have catch a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == 2:
        #damages the player
        print("You have jumped into the ravine")
        print("Your character has taken 10pt of damage")
        character_health = character_health - 10

    elif v == 3:
        #fighting the monster
        print("You have enter the dungeon")
        print("You saw a Monster which they called the ICE DRAGON")
        answer = input("Which weapon do you want to use to defeat the monster? [1 for Magic Templar Blade/ 2 for Lava Katana]")
        if answer == "1":    
            print("You choose and use the magic templar blade on Ice Dragon")
            icedragon_health = icedragon_health - 50
            print("The Ice Dragon didn't die ")
            print("The dragon spits icy breath directly to you leaving you frozen forever")
            character_health = character_health - 100
            print("The monster's Health: " + str(icedragon_health))
            
        elif answer == "2":
            print("You choose and use the Lava Katana on Ice Dragon")
            print("The Ice Dragon is weak againts fire or extreme heat ")
            icedragon_health = icedragon_health - 100
            print("The Ice Dragon is dead " + str(icedragon_health))
            print("You kill the Ice Dragon and you obtain his power ")
            character_power = character_power + 250
            print("Your character's Power increase by: " + str(character_power))
            character_health = character_health - 0
           
            another = input("what you gonna do next after you defeat the dragon [1 Exit to the dungeon/ 2 Go deep down inside dungeon]")
            if another == "1":
                print("you are already out of the dungeon")

            elif another == "2":
                print("You saw another monster")
                print("The monster is what they called HYDRA")
                
                second = input("Do you want to fight the mighty HYDRA? [1 YES/ 2 run away]")
            if second == "1":
                print("you fight the Hydra and You cut his Heads")
                hydra_health = hydra_health - 30
                print("The Hydra Regain their head by using their regeneration power")
                print("The hydra caught you with his tentacles and then he swallow you")
                character_health = character_health - 100
            else :
                print("You run away back to the exit way of the dungeon but the monster hit you")
                print("You slighty injured")
                character_health = character_health - 30
            
            print("Your character's Health: " + str(character_health))
            break
print("Game Over")