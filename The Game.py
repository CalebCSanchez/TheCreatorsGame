
from IPython.display import clear_output
from random import randrange
import time

wooden_sword = 2
sharpened_wooden_sword = 5
rock_sword = 10
iron_sword = 15
sharpened_iron_sword = 30
diamond_sword = 50
flame_sword = 99

no_clothes = 1
linen_clothes = 3
iron_armor = 5
diamond_armor = 10
god_armor = 99


player_HP = 100
player_ATK = wooden_sword
player_DEF = no_clothes
player_potion = 0



enemy_HP = 10
enemy_ATK = 5
enemy_DEF = 1
enemy_alive = True


def attack(attackedhp, personalatk, attackeddef,statement):
    attackhp = attackedhp - (randrange(personalatk) - (randrange(attackeddef)))
    if attackhp > attackedhp:
        print(statement,"attack missed!")
        return attackedhp
    print(statement,"HP:", attackhp)
    return attackhp

#Intro
print("You wake up. decide to leave the house with a wooden sword in hand. You will try not to die this time.")
time.sleep(4)
print("You remind yourself, \"Don't let your hp go below 100!\"")
time.sleep(3)
print("Walking through the forest a bat appears!")
count = 1

#Game
while(True):
    if enemy_alive == True:
        try:
            choice = int(input("Choose 1 to attack or 0 to quit"))
        except:
            print("You need to choose 1 or 0")
            continue
            
        clear_output()
        if choice == 1:
            enemy_HP = attack(enemy_HP, player_ATK, enemy_DEF, "Enemy")
            if count >= 6:
                count+=1
            if count >= 30 and enemy_HP <= 99999000 and enemy_HP >= 1000:
                print("You notice a sticky note that says \"password\".")
            if count >= 45 and enemy_HP <= 99999000 and enemy_HP >= 1000:
                print("Jesus christ just type \"password\"!")
            if count >= 6 and enemy_HP <= 99999000 and enemy_HP >= 1000:
                print("He seems dazed!")
                time.sleep(2)
                print("You notice the creators laptop standing beside him. Quick get into it the computer!")
                time.sleep(1)
                password = input("Type in the creators password:")
                if (password == "password"):
                    print("You've unlocked his computer! Set his HP low enough to kill him!")
                    enemy_HP = int(input("enemy_HP = "))
                    if (enemy_HP <= 0):
                        print("ERROR HACKING DETECTED LOCKED OUT FOR 1 TURN.")
                    elif enemy_HP >= 1000:
                        print("That's too high! You'll have to set it lower next round!")
                    else:
                        print("Now finish him off!")
                else:
                    print("ACCESS DENIED.")
        
        elif choice == 2:
            quit
        if player_HP <= 10:
            if count == 6:
                print("You n░ed to heal! Call upon the godd░ss of life to he░l!")
                time.sleep(3)
                input("Please type your prayers a░d the goddess may spare your li░e ")
                time.sleep(3)
                print("She has chosen to sp░re you!")
                player_HP = 100
                count +=1
            elif count == 10:
                print("You n░ed to h░a░░ C░░l u░on ░he godd░ss of l░f░ to he░l!")
                time.sleep(3)
                input("░░eas░ typ░ y░░r pr░y░░s a░d th░ g░░░░░░ may sp░r░ ░░ur li░e ")
                time.sleep(3)
                print("S░e ha░ ch░░░n ░o sp░re ░░u!")
                player_HP = 100
                count +=1
            else:    
                print("You need to heal! Call upon the goddess of life to heal!")
                time.sleep(3)
                input("Please type your prayers and the goddess may spare your life ")
                time.sleep(3)
                print("She has chosen to spare you!")
                player_HP = 100

        if enemy_HP <= 0:
            if count == 1:
                print("Killed enemy.")
                time.sleep(1)
                print("Collected: Sharpened Wooden Sword and Linen Clothes")
                player_ATK = sharpened_wooden_sword
                player_DEF = linen_clothes
                time.sleep(3)
                print("You continue to walk until a stone troll now stands in your way!")
                enemy_HP, enemy_ATK, enemy_DEF = 30, 7, 2
                count+=1
            elif count == 2:
                print("Killed enemy.")
                time.sleep(1)
                print("Collected: Rock Sword")
                player_ATK = rock_sword
                time.sleep(3)
                print("You continue to walk until a giant bird now stands in your way!")
                enemy_HP, enemy_ATK, enemy_DEF = 50, 10, 2
                count+=1
            elif count == 3:
                print("Killed enemy.")
                time.sleep(1)
                print("Collected: Iron armor")
                player_DEF = iron_armor
                time.sleep(3)
                print("You continue to walk until a dragon now stands in your way!")
                enemy_HP, enemy_ATK, enemy_DEF = 100, 15, 5
                count+=1
            elif count == 4:
                print("Killed enemy.")
                time.sleep(1)
                print("Collected: Diamond Sword and Diamond Armor")
                player_ATK = diamond_sword
                player_DEF = diamond_armor
                time.sleep(3)
                clear_output()
                print("You continue to walk until...")
                time.sleep(3)
                print("The ground shakes...")
                time.sleep(3)
                print("A god appears before you, defeat it before it destroys the world!")
                enemy_HP, enemy_ATK, enemy_DEF = 50, 10, 2
                count+=1
            elif count == 5:
                print("The god explodes into sunshine. The world seems at peace")
                time.sleep(1)
                print("Collected: Flame Sword and God Armor.")
                time.sleep(3)
                player_ATK = flame_sword
                player_DEF = god_armor
                player_HP = 100
                print("You finally rest upon a grateful universe.")
                time.sleep(3)
                print("Nothing can go wrong with today.")
                time.sleep(3)
                clear_output()
                time.sleep(3)
                print("Then the world goes black. You see, him.")
                time.sleep(2)
                print("The Creator.")
                time.sleep(1)
                print(" ITS CALEB")
                time.sleep(2)
                print("He is trying to delete the world! Stop him before it is done")
                enemy_HP, enemy_ATK, enemy_DEF = 99999999, 99, 10
                count+=1
            elif count >= 6:
                print("CRITICAL STRIKE.")
                time.sleep(1)
                clear_output()
                time.sleep(3)
                print("As the creator is gone, so is the world of which he created. The deletion process is complete.")
                time.sleep(3)
                print("You have defeated your creator, and now you lie in a world of nothingness...")
                time.sleep(6)
                enemy_alive = False
        else:
            if count >= 50:
                print("Your body begins to disintigrate. You have started to disappear as the world around you gets deleted.")
                print("Caleb laughs meniacly at your downfall. You disappear never to b...")
                clear_output()
                break
            player_HP = attack(player_HP,enemy_ATK, player_DEF, "Player")
            if player_HP <= 0:                    
                print("You lose!")
                break

    elif choice == 0:
        print("Thanks for playing!")
        break
    else:
        print("Please press '1' or '0'.")
    
