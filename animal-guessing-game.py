#Animal Guessing Game
#------------------------------------------------------
#Functions
#------------------------------------------------------
def guess(myGuess):
    print(f"I think your animal is {myGuess}")
    goodGuess = input("Was my guess corect? (y/n)")
    if goodGuess == "y":
        print("Hooray!")
    return True

def show_animals():
    animals = ["sheep","tiger","dog","dolphin","jellyfish","shark","cat","dove","snake","deer","gorilla","crocodile","bear","polar bear","duck","lion","rabbit","frog","seagull","hippo","leopard"]
    for i in animals:
        time.sleep(1)
        print(i)
    return
#------------------------------------------------------
import time
import random
again = 0

while again == 0:
    print("Welcome to Deborah's Animal Guessing Game!")
    time.sleep(2)
    rn = str(random.randint(0,9)) + str(random.randint(0,9)) +str(random.randint(0,9))
    #===Username=======================================
    print("Let's create your username! ")
    time.sleep(1)
    first_name = input("Enter your first name: ")
    time.sleep(1)
    username = first_name+rn
    print(f"Your username is: {username}")
    file = open("Usernames.txt","w")
    file.write(first_name+" "+rn)
    file.close()
    #==================================================
    time.sleep(2)
    print("Here are the rules of the game:")
    time.sleep(1.5)
    print("  1#You can only answer with 'y' or 'n'")
    time.sleep(3)
    print("  2#You can't change your animal during the game")
    time.sleep(3)
    print("  3#Answer the questions truthfully\n")
    time.sleep(3)
    print("------------------------------------------------------")
    time.sleep(0.5)
    print(f"Choose an animal from this list:")  #\n{animals}
    show_animals()
    chooseOne = "n"
    while chooseOne=="n":
        chooseOne = input("Have you chosen an animal? (y/n)")
        if chooseOne == "y":
            #ca - chosen animal
            ca = input("Enter your chosen animal: ")
            file = open("Usernames.txt","a")
            file.write (ca+"\n")
            print("You may continue with the game. \n")
            print("------------------------------------------------------")
        else:
            time.sleep(3)
    #------------------------------------------------------
    domestic = input("Is it a domestic animal?(y/n) ")
    if domestic=="y":
        housepet = input("Is it a common household pet?(y/n) ")
        if housepet =="y":
            feline = input("Is it a feline animal?(y/n) ")
            if feline=="y":
                guess("cat")
            else:
                rabbit = input("Is it known for eating carrots?(y/n) ")
                if rabbit =="y":
                    guess("rabbit")
                else:
                    guess("dog")
        else:
            bird = input("Is it a bird?(y/n) ")
            if bird=="y":
                canFly = input("Can it fly?(y/n) ")
                if canFly =="y":
                    seagull = input("Is it known for stealing food?(y/n) ")
                    if seagull =="y":
                        guess("seagull")
                    else:
                        guess("dove")
                else:
                    guess("duck")
            else:
                antlers = input("Does it have antlers?(y/n) ")
                if antlers=="y":
                    guess("deer")
                else:guess("sheep")
    else:
        livesInSea = input("Does it live in the sea?(y/n) ")
        if livesInSea =="y":
            boneless = input("Is it boneless?(y/n) ")
            if boneless =="y":
                guess("jellyfish")
            else:
               rNile = input("Can it be found in the river Nile?(y/n) ")
               if rNile =="y":
                   crocodile = input("Does it have scaly skin?(y/n) ")
                   if crocodile =="y":
                       guess("crocodile")
                   else:
                       guess("hippo")
               else:
                   mammal = input("Is it a mammal?(y/n) ")
                   if mammal =="y":
                       guess("dolphin")
                   else:
                       shark = input("Can it have a large set of sharp teeth?(y/n) ")
                       if shark =="y":
                        guess("shark")
                       else:
                            guess("frog")
        
        else:
            bigCat = input("Is it a big cat?(y/n) ")
            if bigCat=="y":
                lion = input("Does it have a mane?(y/n) ")
                if lion =="y":
                    guess("lion")
                else:
                    leopard = input("Is it spotty?(y/n) ")
                    if leopard =="y":
                        guess("leopard")
                    else:
                        guess("tiger")
            else:
                poisonous = input("Can it be poisonous?(y/n) ")
                if poisonous =="y":
                    
                    guess("snake")
                else:
                    polarBear = input("Does it live in the Arctic?(y/n) ")
                    if polarBear =="y":
                        guess("polar bear")
                    else:
                        guess("gorilla")        
        #-------------------------------------------------------
                time.sleep(0.2)
        play = input("Do you want to play again? (y/n)")
        if play == "y":
            time.sleep(0.5)
            again=0
            print("\n ------------------------------------------------------ \n")
        else:
            again=1
            time.sleep(0.5)
        
print("Thank you for playing this game!")
