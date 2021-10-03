import random
#sample text-based game with simple conditional statement
character_health = 100
icedragon_health = 100
character_power = 25
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
        print(" ")
        
        answer = input("Do you want to take the power elixir from the ice dragon? choose your weapon [1 for Lava Katana/ 2 Ice blade]")
        if answer == "1":
            print("You kill the Ice Dragon by using the Lava Katana")
            print(" ")
            print("But you used your all power and slightly damage your health to defeat that monster")
            character_power = character_power - 25
            print("Character's Power is decreased and went to : " + str(character_power))
            character_health = character_health - 10
            print("Character's Health : " + str(character_health))
            print("  ")
            icedragon_health = icedragon_health - 100
            chance = random.randint(0,9)
            if chance > 6:
                item = "elixir"
                print("You found an elixir ")
                character_power = character_power + 200
                print("Character's Power is increased by 200, Current Power: " + str(character_power))
            else:
                print("There is no elixir in this dragon")

        elif answer == "2":    
            print("You choose and use the Ice Blade on Ice Dragon")
            
            print("The Ice Dragon didn't die and absorb the power of your weapon")
            print("The dragon spits icy breath directly to you leaving you frozen forever")
            character_health = character_health - 100
            
        break
           
            
    print("Your character's Health: " + str(character_health))
print("Game Over")